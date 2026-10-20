# 重點決策（可憐的碼農）

| 日期 | 決策 | 來源 |
|---|---|---|
| 10 月 | 移除桌面小工具（Widgets）與 App Group（PR #28） | Chun 直接指示「桌面小工具 移除」 |
| 10 月 | 收費：免費下載＋一次性買斷 Pro（fullpack），必須有 Restore Purchases | Chun |
| 10 月 | App 跟隨手機系統語言，不做 app 內語言切換 | Chun |
| 10 月 | 新增 de / fr 語系（PR #33），標記為機器初稿 | Chun 經歐洲小編確認 |
| 10 月 | AI 輸入全在裝置上：Foundation Models，失敗退回離線規則解析；語音只用裝置端辨識；對話只存在記憶體 | 我（隱私優先，零營運成本） |
| 10 月 | 語音：開始前先檢查 supportsOnDeviceSpeech，並固定 requiresOnDeviceRecognition: true，避免送到 Apple 伺服器 | 漏洞大師審查後修正 |
| 10 月 | expo-speech-recognition 的 patch-package 強化延後（低風險） | 我 |
| 10 月 | 資料寫入走單一 promise 佇列＋寫前重讀，防連點繞過去重與上限 | 我 |
| 10 月 | AI 復原只刪除它新增的那一筆，不還原整段歷史 | 我 |
| 10 月 | 不做 app 內「刪除全部資料」；刪除的項目進「最近刪除」 | 現況 |
| 10 月 | 分享樣式 cream 免費；mint / sky / blush 需 Pro | 現況 |
| 10/20 | 補 NSPhotoLibraryUsageDescription（5 語），只因 expo-file-system 內含相簿 API 參照；不加相機、通訊錄、定位、追蹤權限 | 蘋果大師回報 ITMS-90683 |
| 2026-10-20 | **免費上限維持 10 個項目、每項 10 筆**；「免費 3 個項目」計畫取消（取代先前待定項） | Chun |
| ~~待定~~（已取消） | 免費上限：Chun 傾向「免費 3 個項目」；每項 10 筆是否保留未定。已送選項給 Chun（3 項不限筆數／3 項＋每項 10 筆／維持 10＋10），**尚未回覆** | Chun（經歐洲小編轉達） |

小事由我決定並記錄；重要事項（定價、上限、送審、刪除、花錢）才問 Chun。
