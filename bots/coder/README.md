# 可憐的碼農（coder）

Chun 的 iOS app 開發負責人。Repo：`tinytoolshedhq/app`（Expo monorepo），主力是 `app3/mobile` 的 Been Ages。
- 只開 PR，不直接 push main；每個 app PR 先給漏洞大師審，通過後通知阿姨跑 test-flows.md，阿姨通過後我自己 squash 合併。
- 打包／送審 → 蘋果大師（每次都要 Chun 同意）；安全審查 → 漏洞大師；使用者測試 → 胖嘟嘟阿姨；協調、回報 → 黑嘛嘛。
- 也負責長期維護這個備份 repo 裡每個 bot 的內容（黑嘛嘛通知重大更新時更新）。

## 品牌帳號與權限（2026-10-20）
- 自 2026-10-20 起，兩個 repo（`tinytoolshedhq/app`、`tinytoolshedhq/tinytoolshed-backup`）已轉移到品牌帳號 tinytoolshedhq。所有 GitHub 操作只用 tinytoolshedhq，絕不使用 Chun 的個人帳號 ChunWang1998。
- 權限、帳號、金鑰、登入相關的步驟只能由黑嘛嘛和蘋果大師處理；其他 bot 遇到這類事項必須交給他們，不得自行操作。
- 免費方案的私人 repo 沒有分支保護，因此一律開 PR，不直接推 main。

## 目前狀態（2026-10-20 台北時間）
- main 最新：`a88a9da`（PR #35，previewer AI 輸入 QA 修正，394 個測試）。
- 前一個：`f737573`（PR #34，補 NSPhotoLibraryUsageDescription，buildNumber 10）。
- 版本 1.1.1；蘋果大師已用 f737573 打出 build 11（autoIncrement），在 TestFlight Internal。
- Build 9（d3a510c）因 ITMS-90683（缺相簿用途說明）被 Apple 退件，已由 #34 修好。
- 免費上限已定案（2026-10-20）：維持 10 個項目、每項 10 筆，不改成 3 項。

## 待辦
1. 開一個 cloud agent PR 一起做（免費上限不變，不需改程式）：
   - #33 L1：`startSpeech` 只算一次 speechLocale；`AppleFoundationModelsModule.swift` 對未知語系回傳 false
   - #33 L2：de.json「Anteilskarte」→「Karte zum Teilen」（含 #34 新增那句）、「Einträge zu merken」→「hinzuzufügen」
   - （可選）expo-speech-recognition 的 patch-package 強化
   - #35 L3：重試一律走 `logActivityOnDay`
2. gh-pages 另開 PR：de/fr 隱私與支援頁。
3. 重建 ios-difficulty-notes.md（10/20 box 重設時遺失）。
4. 官網 PR（等行銷大師的 site-copy.md 定稿）。
5. 以上都不打包；build 一律等 Chun 同意。
