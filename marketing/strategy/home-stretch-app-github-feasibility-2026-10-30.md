# 個人化居家伸展 App｜GitHub／技術可行性調查（app-theme-process 第 6 項，2026-10-30，台北時間）

前提：Chun 已決定不拍真人影片，改用插圖加語音。技術棧是 Expo managed、一個 app 一個資料夾、EAS build、expo-iap 一次買斷、資料存本機、不用登入。
星數和最後更新時間是 2026-10-30 從 GitHub API 抓的。授權沒有標「已核實」的，正式使用前要再打開 LICENSE 檔看一次。

## 1. 動作庫與插圖素材

| 來源 | 授權 | 付費 app 可商用？ | 註記 |
|---|---|---|---|
| [yuhonas/free-exercise-db](https://github.com/yuhonas/free-exercise-db)（約 2.1k★，2026-09 更新） | Unlicense（GitHub API 已核實） | 可以，不用署名 | 800 多個動作，JSON 加照片。伸展只佔一部分（有 category: stretching），圖是真人照片，風格不符。適合拿**動作清單和欄位設計**當參考，圖不要用。 |
| [wger-project/wger](https://github.com/wger-project/wger)（約 7.2k★，2026-10-29 還在更新） | 程式碼是 AGPL-3.0；動作資料和圖片依每筆標示，多數是 CC BY-SA | 程式碼**不要**引進 app（AGPL 會傳染）。資料可以商用，但要署名而且衍生物要用相同授權（SA） | API 有 383 張圖，有些授權欄位是空的，**授權不清**。伸展動作少。不建議用。 |
| [ExerciseDB/exercisedb-api](https://github.com/ExerciseDB/exercisedb-api)（約 740★，2025-11 之後沒更新） | 程式碼 AGPL-3.0；GIF 來自商業資料（RapidAPI 付費方案） | **不可以**，或授權不清 | 圖源有版權疑慮。排除。 |
| [Open Peeps](https://www.openpeeps.com/) / [Humaaans](https://www.humaaans.com/)（Pablo Stanley） | CC0 | 可以，不用署名 | 可以組合人物姿勢，但沒有標準的伸展動作，畫得也不夠精確，要大量自己改。適合放在空狀態頁或宣傳圖。 |
| [unDraw](https://undraw.co/license) | 自訂授權：可以免費商用，不用署名，但不能拿來做成競爭的素材庫 | 可以 | 有幾張瑜伽／健身的場景圖，沒有逐步驟的動作圖。只能拿來當裝飾。 |
| [Storyset](https://storyset.com/) / Freepik | 免費版要署名；Premium 才能不署名 | 有條件 | 不建議，因為署名和授權條款比較麻煩。 |
| CC BY-NC 的素材（例如一些瑜伽姿勢插圖包） | NC | **不可以**（付費 app 算商用） | 只要看到 NC 一律排除。 |

**結論**：沒有現成又能商用的「伸展動作插圖庫」可以直接拿來用。建議**自己做 40–60 個動作的簡單 SVG 線條插圖**（統一風格，每個動作 1–3 個步驟畫面），文字和欄位結構參考 free-exercise-db（Unlicense）。工時大約佔整個 app 的 40%。如果改用 AI 生成圖，要確認工具條款允許商用，而且要人工檢查動作有沒有畫對（錯的姿勢有受傷風險）。

## 2. Expo 計時、語音、提醒

- **計時**（JS 計時器）：iOS 進背景或鎖螢幕後，`setInterval` 會被暫停。做法是**記下開始時間戳**，用 `Date.now()` 和目標時間算出剩下幾秒；回到前景時用 [AppState](https://reactnative.dev/docs/appstate) 校正。不要依賴 tick 累加。螢幕可以用 [expo-keep-awake](https://docs.expo.dev/versions/latest/sdk/keep-awake/) 讓它不自動鎖（Expo Go 可用）。[expo-background-task](https://docs.expo.dev/versions/latest/sdk/background-task/) 不適合做秒級的計時。
- **語音引導**：[expo-speech](https://docs.expo.dev/versions/latest/sdk/speech/)（MIT，Expo Go 可用），底層是 iOS AVSpeechSynthesizer。系統內建的聲音**可以離線用**，支援 en、ja-JP、ko-KR、zh-TW（Mei-Jia）、zh-HK，可以用 `getAvailableVoicesAsync()` 選聲音。
  - 限制：鎖螢幕或在背景時要繼續講話，要在 Info.plist 的 `UIBackgroundModes` 加 `audio`，還要在背景時維持音訊工作階段。JS 在背景被暫停，就**沒辦法準時排下一句**。所以 v1 的設計是：**使用中保持螢幕開著（keep-awake）**，背景時改用通知提醒「下一個動作」。
  - 和音樂混音：可以用 [expo-audio](https://docs.expo.dev/versions/latest/sdk/audio/) 的 `setAudioModeAsync`，設定 `interruptionMode: 'duckOthers'` 和 `playsInSilentMode: true`，讓 Spotify 之類的音樂降低音量，而不是被中斷。expo-speech 有沒有完全照這個音訊工作階段走，要上實機測。
- **提醒**：[expo-notifications](https://docs.expo.dev/versions/latest/sdk/notifications/) 的本機排程通知（DAILY 或 WEEKLY trigger），不需要推播伺服器。iOS 一個 app 最多 64 個待發通知。Expo Go 上本機通知可以用（遠端推播不行），這套用不到推播。
- 全部都有 Expo 官方套件（[expo/expo](https://github.com/expo/expo)，約 53k★，MIT），**v1 不需要自訂原生模組**。

## 3. 本機規則加權重排課表

找不到成熟又通用的開源「伸展課表引擎」。這個邏輯很簡單，自己寫一個純 TS 函式就好，好寫單元測試，也符合我們的測試習慣。

演算法草稿：
1. 每個動作的標籤：部位[]、強度 1–3、姿勢（站／坐／地板）、秒數、禁忌（例如膝痛不做深蹲類）。
2. 過濾：去掉有禁忌的、不符合目前環境的（例如辦公室只做站或坐的動作）。
3. 打分數：`score = 部位符合 3 + 目標符合 2 + 難度接近柔軟度自評 1 − 最近 48 小時做過 × 1.5 − 跳過次數 × 0.5 + 一點亂數`。
4. 依分數挑動作，加起來不超過可用時間（5、10、15 分鐘）。順序是：先熱身（強度 1）→ 主要 → 放鬆。同一個部位不要連著排。
5. 回饋：完成就加權重；跳過或回報「太難」就降權重，也降難度。存在 AsyncStorage 或 [expo-sqlite](https://docs.expo.dev/versions/latest/sdk/sqlite/)。
6. 每週「重測」問卷會重新設定柔軟度，對應 GOWOD 的「評估 → 課表 → 重測」。

## 4. （選做）本機姿勢偵測

- 方案：[react-native-vision-camera](https://github.com/mrousavy/react-native-vision-camera)（約 9.6k★，MIT，2026-10-29 還在更新）的 frame processor，加上 MediaPipe Pose（[google-ai-edge/mediapipe](https://github.com/google-ai-edge/mediapipe)，約 37k★，Apache-2.0），或 Apple Vision 的 `VNDetectHumanBodyPoseRequest`（社群 plugin 品質不一）。
- 限制：**需要 dev build，Expo Go 不能用**。每次改原生都要 EAS build，而每次 build 都要 Chun 同意。還要加相機權限的說明。影格都在本機處理，不上傳，隱私上可以接受，但審核會問。伸展動作是靜態、角度大的姿勢，偵測準確度和「姿勢對不對」的判斷規則都要花時間調。
- 難度：**高（4/5）**，估計 2–4 週。**v1 不做**，等 v2 銷量證明需求再說。

## 5. 總結：**Conditional Go（有條件可做）**

條件：
1. 插圖自己做或用可以商用的 AI 生成，40–60 個動作，不用任何 NC 或授權不清的素材。每個素材的來源和授權記在 `assets/LICENSES.md`。
2. v1 只用 Expo Go 相容的套件（expo-speech、expo-notifications、expo-keep-awake、expo-audio、expo-sqlite），不做姿勢偵測，不用 AI API。
3. 使用中保持螢幕開著，背景計時以時間戳校正。實機要測：鎖螢幕、靜音鍵、和音樂一起播。
4. 要附安全聲明（不是醫療建議，痛就停），文案不寫「AI」。

工時估計：程式大約 1.5–2 週（計時、語音、排課表、iap、本機紀錄），插圖和文案 1–2 週，合計大約 3–4 週。
風險：插圖工時（最大）、TTS 在背景的行為、只有插圖用戶看不懂（要靠步驟文字和常見錯誤提示補）、四種語言的語音品質。
建議 v1 範圍：40 個動作、3 種時長、部位／目標問卷、規則排課表、語音倒數、每日提醒、連續天數、一次買斷解鎖全部動作和自訂課表。
