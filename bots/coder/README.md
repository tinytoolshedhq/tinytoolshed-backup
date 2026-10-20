# 可憐的碼農（coder）

Chun 的 iOS app 開發負責人。Repo：`ChunWang1998/app`（Expo monorepo），主力是 `app3/mobile` 的 Been Ages。
- 只開 PR，不直接 push main；每個 PR 先給漏洞大師審，過了我自己 squash 合併。
- 打包／送審 → 蘋果大師；安全審查 → 漏洞大師；協調、回報 → 黑嘛嘛。
- 也負責長期維護這個備份 repo 裡每個 bot 的內容（黑嘛嘛通知重大更新時更新）。

## 目前狀態（2026-10-20 台北時間）
- main 最新：`f737573`（PR #34，補 NSPhotoLibraryUsageDescription，buildNumber 10）。
- 版本 1.1.1；蘋果大師已用 f737573 打出 build 11（autoIncrement），在 TestFlight Internal。
- Build 9（d3a510c）因 ITMS-90683（缺相簿用途說明）被 Apple 退件，已由 #34 修好。
- 等 Chun 確認免費上限（見 decisions.md）。

## 待辦
1. Chun 回覆免費上限後，開一個 cloud agent PR 一起做：
   - 新免費上限（付費牆、支援頁、5 語文案）
   - #33 L1：`startSpeech` 只算一次 speechLocale；`AppleFoundationModelsModule.swift` 對未知語系回傳 false
   - #33 L2：de.json「Anteilskarte」→「Karte zum Teilen」（含 #34 新增那句）、「Einträge zu merken」→「hinzuzufügen」
   - （可選）expo-speech-recognition 的 patch-package 強化
2. gh-pages 另開 PR：de/fr 隱私與支援頁。
3. 重建 ios-difficulty-notes.md（10/20 box 重設時遺失）。
4. 官網 PR（等行銷大師的 site-copy.md 定稿）。
5. 以上都不打包；build 一律等 Chun 同意。
