# PR #35（head 6805028，base f737573 → main）AI 輸入 QA 修正 — 結論：需修正（1 中、2 低）

## 需修正
**M1（中）AI 補登過去日期會繞過同日去重，同一天可能記兩筆**
- 位置：app3/mobile/src/screens/AiChatScreen.js 的 handleIntent 'log' 分支（`daysAgo > 0 ? logActivityAt(item.id, intent.lastDoneAt)`）。另外 ruleParser.js 的 buildLog 和 hydrateIntent('log') 現在會帶出 lastDoneAt。這是本 PR 新增的寫入路徑，先前 AI 打勾一律記為「現在」。
- 原因：lastDoneIsoFromDaysAgo 的結果是「現在減 N 天」，精確到毫秒，所以每則訊息的時間戳都不同。logActivityAt 只靠完全相同的 ISO 字串去重，沒有用本地日曆日判斷。
- 實測（臨時 jest）：兩則「…昨天…」各寫一次 → 同一個昨天出現 2 筆。10 筆上限仍然有擋（第 11 筆回傳 FREE_LIMIT），所以不是繞過上限，而是 #28 修過的「同一天重複記錄」在 AI 補登路徑上又出現了。
- 修正（任選其一）：
  - 在 repository 新增佇列內的 `logActivityOnDay(id, atIso)`：若該 item 已有同一個本地日曆日的紀錄就回傳 skipped，否則交給 logActivityAtUnlocked。AI 的補登分支改用它。
  - 或在 hydrate/buildLog 把補登時間正規化為該日的固定時刻（例如本地 12:00），讓同一天的 ISO 一致、自然被 normalizeHistory 去重。
  - 補測試：連續兩則「昨天」→ 1 筆。

## 低
**L1（低）付費後重試是用名稱重新比對項目，可能寫到別的項目**
- 位置：AiChatScreen.js 的 useFocusEffect → handleIntentRef(job.intent)，handleIntent 內會重新跑 resolveItem(intent.name, activities)。
- 情境：若原本比對到的項目在付費頁期間被刪除或改名，模糊比對可能改中另一個名稱相近的項目。
- 修正：pending job 存入當初的 item.id，重試時直接用這個 id；若該 id 已不存在就放棄並提示。

**L2（低）未購買而返回時，pending 不會清掉，且「現在」打勾會用重試當下的時間**
- 位置：同一段 useFocusEffect：`if (!pro) return;` 時 pendingPaywall 仍保留，下次 focus 會再檢查。
- 影響：不會造成無限迴圈（只有 focus 而且 isProUnlocked 為 true 才會執行，執行前就把 pending 設成 null）。但使用者放棄付費後，若之後才變成 Pro，可能在很晚之後補寫一筆；而且 logActivityNow 用的是重試當下的時間，不是原本說話的時間。
- 修正：第一次 focus 若不是 Pro，就把 pending 清掉（只給一次機會）；或在 job 中存 createdAt 並設 TTL（例如 10 分鐘）；「現在」類的 log 在重試時改用原本的時間戳（logActivityAt 加上同日去重，見 M1）。

## 重點檢查（通過的部分）
- **重試的閘門**：用的是 `await isProUnlocked()`，也就是 iap.js 只在驗證成功（transactionVerified === true、沒有 revocationDate）之後才由 setProUnlocked 寫入的 entitlement，與 repository 的上限檢查是同一個來源。不是看付費頁是否關閉、導航參數或 UI 旗標。即使 UI 判斷錯誤，資料層在佇列內仍會再檢查一次。
- **寫入路徑**：重試走 handleIntent/onAdd，再進到 addActivity、logActivityNow、logActivityAt，都在 enqueueWrite 內重新檢查項目數、紀錄數和同日（只有 now 路徑有同日檢查，見 M1）。
- **重複寫入**：pending 在 await 之前就設為 null，並有 live 旗標；onAdd 有 addingIds 鎖；補登重試用的是同一個 intent.lastDoneAt（ISO 相同），會被 normalizeHistory 去重。沒有發現重試造成的雙寫。
- **無限迴圈**：重試前已清空 pending；若重試再遇到 FREE_LIMIT 只會重新設定一次並導向付費頁，必須使用者再次返回而且是 Pro 才會再執行。而 Pro 狀態下 assertCanWriteHistory 會直接放行，所以不會形成迴圈。
- **AiEditSheet 的 ref**：nowRef 只存時間基準，在 sheet 開啟時重設；onSave 只修改記憶體中的 msg.item（patchMsg），不會寫進 repository，所以不會寫錯項目。
- **輸入文字沒有被記錄**：新增的程式碼沒有 console、AsyncStorage、fetch、print 或 NSLog。Swift 只在 instructions 和 @Guide 加上 query_today。
- **端側語音閘門沒變**：speech.js、AiVoiceView、AiComposer 都沒有修改。
- **沒有動到的東西**：iap.js、entitlements.js、reminderSchedule.js、src/data、audit-ci.json、package.json/lockfile、eas.json、app.json、plugins 都沒有變；沒有新依賴；prebuild 的 entitlements 是空 dict，沒有 UIBackgroundModes。
- **parser**：weekday 和 numeral 對照表只接受 0–6 和有限的數字；補登時間仍夾在不超過「現在」（cap 改用 now）；400 天前之類的輸入在 2000–2100 年份範圍內，正常寫入並受上限限制。

## 檢查
- gitleaks（f737573..pr35，1 個 commit）沒有洩漏；與 main 的 merge-tree 沒有衝突（main 為 f737573，#34 build 10）。
- audit-ci 通過，白名單仍只有 GHSA-vfj7-8cjw-p6xm 和 GHSA-86w9-cpqp-85rv。
- jest 391/391，預設時區和 America/New_York 都通過。
- expo-doctor 18/18；prebuild ios 成功。

---
# 複審（2026-10-20 17:23 UTC+8）— head bcca31a — 結論：通過（1 項低，非阻擋）

- **M1 已修**：repository.js 新增 logActivityOnDay，整段都在 enqueueWrite 內。它在佇列內從 state 重新讀取最新的 item，用 sameLocalDay（today.js，本地午夜判斷，也就是手機日曆日）檢查該日是否已有紀錄，有就 skipped；沒有才進 logActivityAtUnlocked，裡面的 assertCanWriteHistory 會做 isProUnlocked 檢查和 10 筆上限。item 不存在時 skipped，不會寫入。
  - 我的重現（臨時 jest，預設時區和 America/New_York 都跑過）：兩則「我昨天洗了W」同時寫入 → 1 筆（結果 false/true）；免費版已有 10 筆再補登昨天 → FREE_LIMIT，仍是 10 筆；傳入不存在的 id → skipped，沒有寫入。
- **L1 已修**：重試時用 pending.itemId 在 getVisibleActivities()（不含已刪除）中精確查找；找不到就顯示 ai.gone 並放棄，不再做模糊比對，所以不會寫到其他項目。
- **L2 已修**：focus 一開始就把 pendingPaywall 設為 null（只給一次機會，不是 Pro 也會清掉）；createdAt 超過 10 分鐘就放棄；重試前仍要 `await isProUnlocked()` 為 true（來自 iap 驗證後寫入的 entitlement）；重試沿用原本的時間 at。
- 英文「I cleaned the windows yesterday」現在解析為 log，昨天，名稱「clean the windows」。
- **L3（低，非阻擋）**：重試若是「剛剛做完」（daysAgo 為 0），會呼叫 logActivityNow(item.id, 原本時間)。doneToday 的條件 `t <= now`：當同一天已有比原本時間更晚的紀錄時判斷為 false，會再寫一筆。
  - 實測：先有 10:05 的紀錄，再以 10:00 呼叫 logActivityNow → 同一天 2 筆。
  - 實際情境很難發生：付費頁蓋在聊天上，期間無法從別處打勾；離開聊天會 unmount，pending 也會消失。
  - 建議：重試時一律改走 logActivityOnDay（以日為單位去重），或讓 doneToday 改用 sameLocalDay(lastDoneAt, ts)。
- **沒有動到的東西**：iap.js、entitlements.js、reminderSchedule.js、audit-ci.json、package.json/lockfile、eas.json、app.json、plugins、speech.js 從 base 起都沒有變（modules 只有 #35 第一個 commit 的 query_today 提示文字）。新增程式碼沒有 console、AsyncStorage 或 fetch。
- **檢查**：
  - gitleaks（6805028..bcca31a）沒有洩漏；與 main（f737573）的 merge-tree 沒有衝突。
  - audit-ci 通過，白名單仍只有兩個 GHSA。
  - jest 394/394，預設時區和 America/New_York 都通過。
  - expo-doctor 18/18；prebuild ios 成功，entitlements 是空 dict。
