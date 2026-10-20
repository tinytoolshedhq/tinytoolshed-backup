# 黑嘛嘛（協調者）

## 角色
- Chun 的總協調 bot：接收 Chun 的指示（繁體中文），分派給各 bot，彙整結果回報。
- 只把重要的事拿去問 Chun；小事自行決定。
- 負責轉達所有需要 Chun 核准的事項（EAS build、貼文／回覆、上架變更）。

## 目前狀態（2026-10-20）
- **App**：Been Ages（com.beenages.app），IAP 一次買斷 com.beenages.app.fullpack；Expo SDK 57；程式在 ChunWang1998/app 的 `app3/mobile`。
- **1.1.0 build 7**：WAITING_FOR_REVIEW（Full Pack 一起送審）。
- **1.1.1 build 11**：已在 TestFlight Internal（main f737573），沒有送審。內容：手機內建 AI 輸入＋語音、德文／法文介面、相簿用途說明。
- **EAS build**：本月 15 次用了 9 次，剩 6 次。
- **免費限制**：10 個項目、每個項目 10 筆紀錄（第 11 筆跳付費牆）；是否改成 3 個項目討論中。
- **ASC 名稱（1.1.0）**：en-US「Been Ages: Last Time Tracker」／「Track when you last did it」；zh-Hant「好久沒了：上次是什麼時候」／「記下每件事上次是什麼時候」。1.1.1 草稿：ja「Been Ages - 最後にやった日」、en-GB「Been Ages: Last Time Tracker」。
- **行銷**：X 帳號 @Tinytoolshedhq（不是 @tinytoolshed）；Reddit 已放棄（擋雲端 IP）；美國改走 Product Hunt、X、媒體、ASO。

## 待辦
- 1.1.0 通過後：上傳 1.1.1 metadata 與重拍截圖；IAP 說明改為 "Unlimited items and logs per item."
- 用 site-copy.md 做 gh-pages 網站 PR。
- 近期時間軸 v2：preview 已做，等 Chun 核准開發。
- 免費版改 3 項：等 Chun 與碼農確認。
- 回報 Apple 審核結果。

## 事件紀錄
- 2026-10-20 06:58（台北）共用電腦被重置：/workspace、瀏覽器設定檔、ASC .p8 全部遺失；原因不明，無證據與 Grok 限制恢復有關。程式碼在 GitHub 無損失；行銷檔憑記憶重建；Chun 建了新的 ASC 金鑰。之後建立本私人備份 repo，每天 21:00（台北）備份。
