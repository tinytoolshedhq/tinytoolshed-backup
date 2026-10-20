# 審查流程

1. 碼農用 SendToAgent 送來 PR 編號和 head commit。
2. 小 PR（只改設定或文字）：直接讀 diff。其他 PR：clone 下來完整檢查：
   - gitleaks 掃 PR 的 commit 範圍。
   - audit-ci：白名單只能有 braces 和 node-forge，不能放寬。
   - jest：預設時區和 TZ=America/New_York 各跑一次。
   - git merge-tree 檢查衝突。
   - `npx expo prebuild --platform ios` 和 expo-doctor。
   - 檢查 entitlements、Info.plist 權限、eas.json、lockfile 的來源與 integrity、install scripts。
   - 確認 IAP（iap.js、entitlements.js）和 reminderSchedule.js 沒被改動。
   - 檢查隱私權頁和支援頁（gh-pages）的內容和實際行為是否一致。
3. 有疑慮時寫臨時測試重現（不提交）。
4. 報告寫成 /workspace/security/pr-<n>-review.md，每個問題寫位置、風險等級（高／中／低）和修法。
5. 結論用 SendToAgent（priority true）回給碼農，明確寫「通過」或「需修正」；需修正就等碼農修完再複審。
6. 通過後由碼農轉交胖嘟嘟阿姨跑 `bots/user-tester/test-flows.md`。安全審查不是最後關卡；合併與 EAS 還要等阿姨通過。
7. 只有重要的結果才用繁體中文簡短告訴 Chun，例如安全漏洞、可以上線、需要他決定的事。
8. 每次 EAS build 都要 Chun 先同意，每月額度 15 次；我會提醒碼農，但不碰 build。
