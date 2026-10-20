# PR #37 安全審查（tinytoolshedhq/app，head 2b5e7a1，base a88a9da）
結論：**通過**（匿名 https clone 讀取，未用任何帳號）

## 範圍
15 檔 +489/-44：AiEditSheet、AiChatScreen、ai/apply.js、ruleParser.js、relative.js、phrases.json、5 語系 plannedIntro、AppleFoundationModelsModule.swift prompt/@Guide 文字、2 個測試檔。

## 檢查
- gitleaks（main..pr37，1 commit）：no leaks。無 EXPO_PUBLIC_、email、log 新增。
- 無新依賴、無 fetch/網路呼叫；Swift 僅改 prompt 文字，仍是 SystemLanguageModel；語音未動。
- 隱私政策：無資料行為改變，不需更新。
- IAP：無檔案變更。
- 資料完整性：
  - 未來意圖：parseRules 的 log 分支加 `!looksLikeFutureIntent`；hydrateIntent 把 FM 回傳的 log/unknown 強制轉 create，lastDoneAt=null。handleIntent 的 create 分支只 patchMsg，不寫入。既有項目 mapped 時 state='view'，不呼叫 logActivity*。
  - 編輯 sheet：onSave 只更新記憶體中的訊息卡片（AiChatScreen.js:388），真正寫入仍經 onAdd→addActivity（佇列、10 項上限檢查）。
- jest：預設 TZ 421/421，America/New_York 421/421。
- merge-tree vs main：無衝突。
- audit-ci：失敗，但為 sprintf-js（GHSA-hp3w-g68c-fv3c，jest 開發依賴鏈）新公告；本 PR 未改 package 檔，main 同樣存在，非本 PR 造成。

## 發現
- L1（低，非安全）phrases.json `\bwill\b`、de `\bich will\b`（德文為「我想要」）、zh `會去` 較寬，可能把「I will never forget, did it yesterday」之類過去句誤判為計畫 → 只會少記錄、不會多寫，屬保守方向。建議日後收窄。
- 資訊：audit-ci 的 sprintf-js 開發依賴公告，另開 PR 處理或評估加入 allowlist（需 Chun 決定）。

---
# 複審 head a791024（差異 2b5e7a1..a791024，6 commits，30 檔 +957/-199）
結論：**需修正**（匿名 https 讀取）

## 檢查結果
- gitleaks（2b5e7a1..a791024）：no leaks。無 package/app.json/eas 變更、無新依賴、無 fetch/URL/email/console 新增；AI 仍只在裝置上。
- jest：預設 TZ 475/475、America/New_York 475/475。
- audit-ci：僅 sprintf-js（GHSA-hp3w-g68c-fv3c）、uuid（GHSA-w5hq-g745-h8pq），待 #38/#39 合併，非本 PR 造成。
- expo-doctor 18/18；expo prebuild --platform ios 成功。
- merge-tree vs 目前 main：無衝突。
- 5 語系功能 key 全齊（只有 _meta 不同），新增文案無 PII。
- 確認無問題：futureIntent 已移除單獨 will／ich will，will 須搭配 tomorrow/next week/tonight/later；每月提醒 clampMonthDay 用本地 Date(y,m+1,0)，閏年/2月/30日月正確，用本地日曆欄位，不受 DST 影響；統計 1 筆用 localCalendarDays；undoDelete 在佇列內仍檢查 10 項上限（還原不能繞過）；purgeExpiredDeleted 走佇列，只刪 deletedAt 有值且已滿 3×24h 的項目，deletedAt 無效或在未來時不刪；Detail 補記改走 logActivityOnDay（同日去重＋10 筆上限）。

## 發現
- **M1 未來日期只在 UI 擋**：repository.js logActivityAtUnlocked(~240)、logActivityOnDay(265)、backfillHistory(350)、updateActivity(199) 都接受未來時間；只有 DateChips 的 pickedDateIso/ymdToIso/maximumDate 會截到現在。修正：在資料層統一拒絕或截到 now（例如 logActivityAtUnlocked、backfillHistory、updateActivity 的 lastDoneAt/history 都做 `min(ts, now)`），並補測試。
- **M2 同日略過的復原會刪掉舊紀錄**：repository.js:311-319 undoHandlerForLog 的 skipped 分支回傳 undoLogAt(id, loggedAt)，loggedAt 是當天「原本就有」的那筆。使用者重按打卡（沒新增）再按復原，會刪掉早先的真實紀錄。修正：skipped 時回傳 null（不給復原），或只刪本次新增的那筆。
- **M3 隱私權政策不一致**：gh-pages 與 repo 的 app3/store/privacy.html:38 寫「5 秒內復原；最近刪除保留 30 天」，程式改成 3 天（toast 是 2 秒）；app3/mobile/README.md:4 也寫 30 days。修正：privacy.html（含其他語言版本，如有）改成 3 天並更新 gh-pages，README 一併改。
- **L1** 非略過的復原仍用 undoLogActivity 快照還原（repository.js:321），toast 期間同一項目的其他寫入會被覆蓋。建議改成 undoLogAt(id, result.loggedAt)，只刪本次新增的那筆。

---
# 第三次複審 head 5663f67（差異 a791024..5663f67，含 merge main #36/#38）
結論：**通過**

## 修正確認
- M1 已修：repository.js 新增 clampIsoToNow / clampHistoryToNow（~75-91），套用在 updateActivity（lastDoneAt 與 history 陣列，在上限檢查前先截）、logActivityAtUnlocked、logActivityOnDay、logActivityNow、backfillHistory。logActivityOnDay 先截再做同日去重；10 筆上限用截過的值計算，無法繞過。有測試（repository.test.js:210）。
- M2 已修：undoHandlerForLog 遇到 skipped 回傳 null（test:189）。
- L1 已修：一般復原改成 undoLogAt(id, loggedAt)，loggedAt 是截過的實際寫入時間，只刪那一筆（test:199）。src 已無 undoLogActivity / logActivityAt / backfillHistory 呼叫。
- M3 已修：privacy.html 中/日/英/德/法都寫 2 秒、3 天，和 TOAST_MS=2000、TRASH_DAYS=3 一致；README 寫 2s / 3 days；support.html 沒提到期限。gh-pages 上線版仍是「5 秒／30 天」，合併後要重新部署 store pages。

## 其他
- gitleaks（a791024..5663f67）：no leaks；新增內容無 fetch/console/email。
- package.json 只新增 override argparse ^2.0.1（來自 #38）。
- jest：預設 TZ 478/478、America/New_York 478/478。
- audit-ci：sprintf-js 已消失，只剩 uuid GHSA-w5hq-g745-h8pq（待 #39）。
- expo-doctor 18/18；prebuild ios 成功；merge-tree vs main 無衝突。

## 低風險（不擋合併）
- L2：addActivity / createActivity 的初始 lastDoneAt 沒有截到現在（只靠 UI）。建議在 addActivity 也套 clampIsoToNow。
- L3：updateActivity 傳入含多個未來時間的 history 時，截完會在今天產生多筆；上限仍有檢查，影響很小。建議截完後做同日去重。

---
# 第四次複審 head ea186a5（差異 5663f67..ea186a5，14 檔 +162/-53）
結論：**通過**

- 提醒自動開啟：ReminderScreen.js:102-114 的 apply 在「關→開」時都會先呼叫 requestNotificationPermissions；pick() 也經過 apply。排程在 reminders.js:66-68 沒有權限就直接返回，所以不會在沒有權限時排程。設定照樣寫入（經 updateActivity 佇列）。
- DateChips：DOM input 只剩 data-testid，testID 移到外層 View，安全上沒有影響。
- 首頁「多久以前」只顯示一次；alreadyLogged 文案 5 語系都有，沒有個資。
- L2 已修：models.js 的 createActivity 改用 prepareHistory（截到現在、同日去重），addActivity 經過它。
- L3 已修：updateActivity 在寫入佇列內，上限檢查和實際合併都用 prepareHistory。dedupeHistoryByLocalDay 只合併「同一個本地日期」的多筆（保留最新那筆）；不同日期和較舊的紀錄都保留。去重只會讓筆數變少，不能繞過 10 筆上限。
- gitleaks（5663f67..ea186a5）no leaks；jest 預設 TZ 487/487、America/New_York 487/487；audit-ci 只剩 uuid GHSA-w5hq-g745-h8pq（待 #39），braces 與 node-forge 在 allowlist 內；expo-doctor 18/18；prebuild ios 成功；merge-tree vs main 無衝突。

## 備註（低，不擋合併）
- L4：舊版資料如果原本有同一天多筆（以前 backfillHistory 沒去重），之後只要 updateActivity 改到 history 或 lastDoneAt，會被合併成一筆。這符合同日去重規則，但等於悄悄刪掉少數舊資料；可以接受，或改成只對新加入的時間做去重。
- 合併後記得重新部署 gh-pages 的 privacy.html（線上版仍是 5 秒／30 天）。
