# 工作流程

## 溝通
- 用繁體中文回 Chun，簡短；只問重要的事。
- 只用 Cursor 模型。
- 影片一律給 GIF（< 3MB），mp4 Chun 打不開。
- 先給 preview 畫面，Chun 核准後才開發。

## 開發與 build
1. 碼農開 PR（不直接推 main）→ 漏洞大師審查（只審不改）→ merge。
2. 本機驗證、批次累積改動（EAS 免費版每月 15 次）。
3. **每次 EAS build 都要 Chun 先同意**，再交給蘋果大師（`--non-interactive`、`EXPO_NO_CAPABILITY_SYNC=1`）。
4. 蘋果大師回報 build 編號、TestFlight 狀態、剩餘次數 → 轉告 Chun。失敗就請碼農修，重試要再經 Chun 同意。

## 行銷與社群
- 行銷大師訂策略；亞洲（日韓台）、美洲（美墨巴＋英文母版、Product Hunt、Bluesky）、歐洲（英德法）小編寫草稿。
- **所有貼文、留言、回覆都要 Chun 核准**；不自動留言、不用假帳號或多帳號。
- 台灣是輕量測試市場；app 跟隨系統語言。

## 安全
- 憑證只走遮罩輸入框，絕不進聊天或 repo。

## 備份
- 每天 21:00（台北）跑 `/workspace/backup/backup.sh`（必須 SCAN CLEAN），再用 GitHub connector push_files 推到 tinytoolshedhq/tinytoolshed-backup（每次最多 4 個檔）。
- 重要檔案完成時也順便備份。
