# 實作摘要（可憐的碼農）

## Repo 概覽：tinytoolshedhq/app
| 目錄 | App | 說明 |
|---|---|---|
| `app1/game` | 諧音猜猜 | 諧音梗問答，無內購、無敏感權限 |
| `app2/mobile` | 急廁 Go | 找附近有廁所的店；使用期間定位；買斷 fullpack 下載離線資料包 |
| `app3/mobile` | **Been Ages／好久沒了** | 目前主力 |

根目錄 `package.json`／`app.json`／`eas.json` 是空殼；設定都在各 app 目錄。商店支援／隱私頁在 gh-pages。

## Been Ages（app3/mobile）
「上次做這件事是多久以前？」生活記錄器。

### 平台
- Expo SDK 57，最低 iOS 17；版本 1.1.1，main 的 buildNumber 10（EAS autoIncrement）。
- eas.json production / preview 使用 `macos-tahoe-26.5-xcode-26.6` 映像。
- 字型 BeenAgesRounded：Naikai 子集（OFL），由 `scripts/subset-naikai.sh` 產生，兩支字型檢查腳本確認字元覆蓋。

### 功能
- 項目清單、新增／編輯、記錄、提醒、分享卡片、行事曆、最近刪除（垃圾桶）、付費牆。
- 項目圖示由類別決定；state version 3。
- 同一天去重以本地日曆日為準。
- 所有寫入走單一佇列 `enqueueWrite`，寫前重讀（防連點）；新增按鈕有 in-flight 防重複。
- 已移除：桌面小工具與 App Group。沒有 iCloud、沒有鎖定畫面記錄、沒有「刪除全部資料」。
- 資料只存在手機上。

### 免費上限（目前 main）
- `FREE_ACTIVITY_LIMIT = 10` 個項目；`FREE_HISTORY_LIMIT = 10` 筆／每項。
- 超過任一項就開付費牆；第 11 筆記錄以 reason `'history'` 開啟。
- 2026-10-20 定案：維持 10＋10；「免費 3 個項目」已取消。

### 內購（IAP）
- `expo-iap`，非消耗型一次性買斷 `com.beenages.app.fullpack`（Pro）。
- 有 Restore Purchases；`preview` profile 以模擬模式測試。
- Pro 解鎖：無上限、分享樣式 mint / sky / blush（cream 免費）。
- IAP 程式碼原則上不動。

### AI 輸入與語音（全部在裝置上，尚未上架）
- 首頁底部輸入列 → 對話畫面：建立項目、查詢、記錄（可復原）。
- 解析：本地 Swift 模組 `apple-foundation-models`（Apple Foundation Models）；不可用時退回離線規則解析。
- 語音：`expo-speech-recognition`，先 `supportsOnDeviceSpeech(locale)`，一律 `requiresOnDeviceRecognition: true`，不會送到伺服器。
- 對話只存在記憶體，不存檔。
- 復原只刪掉 AI 新增的那一筆。

### i18n
- en、zh-Hant、ja、de、fr（de / fr 為機器初稿）。
- 跟隨系統語言，沒有 app 內切換。
- iOS 權限用途說明（Info.plist）5 語都有：相簿讀取、存相簿、麥克風、語音辨識、行事曆、提醒事項。沒有相機、通訊錄、定位、追蹤。

### 重要 PR
| PR | Commit | 內容 |
|---|---|---|
| #27 | 0221d9c | 1.1.1、worklets |
| #28 | c20869f | 實機問題修正 1–9、移除小工具、buildNumber 8 |
| #29（gh-pages） | a9845c4 | 支援與隱私頁 |
| #30 | d3a510c | AI 輸入＋3 個小修正 |
| #31（gh-pages） | 29b56d5 | 隱私頁 AI 說明 |
| #32 | 4c6e6bb | buildNumber 9 |
| #33 | 431a92f | de / fr 在地化 |
| #34 | f737573 | 補 NSPhotoLibraryUsageDescription（修 ITMS-90683），buildNumber 10 |
| #35 | a88a9da | previewer AI 輸入 QA 修正：AiEditSheet 值改存 ref；付費牆後一定顯示回覆；重試用原項目 id（10 分鐘過期）；`logActivityOnDay` 補登也做同日去重；0 天顯示「今天」；查詢只講天數；解析器修正＋38+ 句測試（共 394 個測試）。待辦 L3：重試一律走 `logActivityOnDay` |

### 踩過的坑
- ITMS-90683：第三方套件（如 expo-file-system）只要 binary 有權限 API 參照，就必須有對應 UsageDescription，即使 JS 沒用。
- 舊 branch 開的 PR 要先 merge origin/main（一般 merge commit）再合併。
