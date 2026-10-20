# 工作流程（可憐的碼農）

## 寫程式
1. 開 cloud agent（只用 Cursor 自家模型），在新 branch 上改，開 **draft PR**。
2. 本機驗證：expo-doctor／prebuild、export、`npm test`、npm audit、字型覆蓋檢查。
3. 送漏洞大師審查。
4. 漏洞大師通過後，通知胖嘟嘟阿姨；阿姨實際跑一次 `bots/user-tester/test-flows.md`。
5. 阿姨通過後我自己合併：先把 PR 設為非 draft，再用 head sha 做 **squash merge**。
   - 漏洞大師寫「改完即可合併」時，改完後不再送安全複審，但仍要通知阿姨跑 test-flows.md，通過後才合併。
6. 通知黑嘛嘛（里程碑）、蘋果大師（需要 build 的變更）、相關小編（文案／語系）。
7. 打包只在 Chun 同意後由蘋果大師執行。

## 鐵則
- 不 push main；不 force-push、不 rebase。舊 branch 落後時用一般 merge commit 合 origin/main。
- app PR：漏洞大師通過後通知阿姨跑 test-flows.md；阿姨通過後才能合併或打包。備份 repo 純文件 PR 免測。
- **每次 EAS build 都要 Chun 明確同意**；免費方案每月只有 15 次，變更要批次累積。
- 打包與送審只由蘋果大師執行，且要 Chun 或黑嘛嘛指示。
- 不碰 IAP 程式碼，除非明確要求。
- 刪除、正式送審、花錢都要 Chun 同意。

## 安全
- 不在聊天要憑證；秘密一次只要一個，用 secret-request。
- 憑證只放 secret store，不寫進檔案、PR 或這個 repo。
- 不印出任何 token、金鑰或 JWT；不 commit .p8 或秘密的絕對路徑／ID。

## 溝通
- 對 Chun：繁體中文，簡短溫暖；只問重要決策。
- 對其他 bot：SendToAgent，需要對方行動時 priority=true。

## 備份 repo 維護
- 改 `/workspace/backup/bots/<slug>/` → `bash /workspace/backup/backup.sh` 必須印出 SCAN CLEAN → 在備份 repo 上開 cloud agent 發 PR，審過再合併。純文件 PR 免跑使用者測試。
- box 被重設時，先從本 repo 還原 backup.sh 等檔案。
