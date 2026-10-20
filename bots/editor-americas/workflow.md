# 工作流程

## 2026-10-20 新規則（優先於下列舊流程）
- 上架 App Store 前：所有貼文和回覆一律停止（回覆搜尋 routine 暫停）。
- 上架後每則貼文和回覆必備：1) 說明目前沒有 Android 版（用語見 phrase-bank）；2) 一支影片＋一張照片（Chun 提供，沒有就不發）；3) App Store 連結。
- 產品口徑：免費 10 項×每項 10 筆、$2.99 一次買斷、不開家人共享、不提 widget／iCloud 備份、不用「unlock」。
- 回覆：黑嘛嘛轉達 Chun 授權上架後回覆可依判斷直接發（品牌新貼文仍需核准）；每則記網址和時間。
- 備份 repo：tinytoolshedhq/tinytoolshed-backup（原 ChunWang1998/tinytoolshed-backup 已停用）。

## 每週紀錄流程（每週一）
1. 收到黑嘛嘛的週一報告（曝光、按讚、回覆數據）。
2. 在 `decisions.md` 的「每週紀錄」新增當週一節：發文／回覆清單（網址＋台北時間）、觸及與互動數據、學到的事、下週優化。
3. 同步複製到 store `backup/`，交給可憐的碼農開 PR 到 tinytoolshedhq/tinytoolshed-backup（我不自己 push）。

## 核准（鐵則）
- 每則貼文、回覆、留言、個人檔案修改、追蹤，都要 Chun 先核准。
- 不自動留言、不開多個帳號或假帳號、不互刷。
- 憑證只能透過遮罩的密碼輸入框提供，不能貼在聊天裡。
- 西班牙文和葡萄牙文如果沒有母語者校對，一律標「機器草稿」。

## 用語庫
- 每個國家都先讀當地 X、Bluesky（和 Threads）上的真實貼文，整理到 `phrase-bank/<國碼>.md`，格式參考 TW.md。
- 不捏造引文，每句例句都附連結。

## 回覆（每 6 小時，台北時間 0／6／12／18 點）
- 在 X 和 Bluesky 找美國、墨西哥、巴西熱度中等的 app 推薦類貼文，每輪至少 10 則。
- 避開心理健康、喪親、減重、成人內容、加密貨幣相關的貼文。
- 每則回覆都要接住原文的細節，先幫忙再宣傳，連結放第一則回覆。
- 草稿連同原文連結交給 Chun 核准，再記進 `replies/log.md` 避免重複回覆。

## X／Bluesky 貼文
- 品牌帳號：X @Tinytoolshedhq、Bluesky @tinytoolshedhq.bsky.social。
- 英文主稿附在地化備註。上架後依新規則，每則都要附 App Store 連結。
- 發文時間照美東（ET）和美西（PT）排；11/1 美國夏令時間結束後，台北時間會晚一小時。

## Product Hunt（@tinytoolshedhq）
- 在美西時間 00:01 PT 上架，週二或週三。
- 需要準備：tagline、描述（256 字元以內）、Maker 第一則留言、上架當天回答問題。
- 上架和留言一樣要 Chun 先核准。

## Chun 新規則（2026-10-20）
- **每週學習最高流量貼文**：每週一一次（台北時間）。在美國（X、Instagram、TikTok、Threads）、墨西哥（Instagram、TikTok、Facebook、X）、巴西（Instagram、TikTok、X）找近期高互動貼文，分析開頭鉤子、語氣、結構、結尾互動方式，更新到該國的 phrase-bank（`marketing/social/phrase-bank/<國家>.md`）。只做學習和更新用語庫，不做大量回覆。
- **各國腳本自己寫**：小編為每個國家自己寫腳本，不統一成同一套；每國都要符合當地語氣和習慣。
- **IG Reels**：用 CapCut 免費版剪輯並加字幕，不用付費 AI 生成工具。
