# PR #45 資安／隱私審查（app4 分貝計，head 91711af）
結論：**需修正**（2 項中低風險，無外洩）

## 檢查結果
- gitleaks（diff 與 app4/mobile 樹）：0 筆。regex：無 key/token/email/電話/EXPO_PUBLIC_；projectId 為全 0 佔位符，bundle 為 com.example.decibelmeter；README 內 ASC ID（6798…759、6798…716）為 main 原有。
- 依賴：無網路／分析／內購套件；src 無 fetch/XMLHttpRequest。
- jest 33/33（預設與 America/New_York）；expo-doctor 18/18；expo prebuild ios 成功，Info.plist 無 UIBackgroundModes；git merge-tree 對 main 無衝突。audit-ci 未設定。
- 麥克風：英文與繁中用途說明皆具體；背景時 pause、回前景才恢復；unmount 時 stop 並關 allowsRecording；enableBackgroundRecording=false。
- 根 README：刪除的行僅為兩張表格（加 app4 欄後重寫）和「目前兩個 app」→「目前幾個 app」，原內容皆保留，無不當刪除。

## 需修正
1. **M1 `.github/workflows/app4-ci.yml` 缺 permissions**：未宣告時 GITHUB_TOKEN 依 repo 預設可能有寫入權。修法：在頂層加 `permissions: contents: read`。（觸發為 pull_request、無 secrets、無 github.event 注入、actions 為官方 @v4、有 paths 篩選，皆可。）
2. **M2 暫存錄音檔未刪、說明不準確**：`src/hooks/useMetering.js` 用 LOW_QUALITY 真的錄成 cache 檔，stop 後未刪除；但用途說明寫「不會儲存錄音」。修法：stop/unmount 後用 expo-file-system 刪除 `recorder.uri`（或每次 start 前清除舊檔），並加測試；或把說明改為「只暫存在本機、用完即刪、不會傳送」。

## 低風險建議
- L1：Android 會帶入 MODIFY_AUDIO_SETTINGS（expo-audio 自帶），上架隱私表註明即可。

---

## 重審 R2：head b635928（增量 91711af...b635928，diff：pr45-r2.diff）

**結論：通過**

- M1 已修：app4-ci.yml 頂層 `permissions: contents: read`；只觸發於 pull_request，沒有 secrets、沒有 write、沒有 pull_request_target；新增 audit-ci 步驟。其他設定都沒有被放寬。
- M2 已修：useMetering 在 start 之前（prepareToRecordAsync 前）、stopRecorder 時和 unmount 時都呼叫 stopAndDiscardCache；stop 前後各記一次 uri 並都刪除；uri 是 null 或空字串時不動作；`idempotent: true`；所有錯誤都吞掉、不會 throw；沒有 console 或 log 輸出路徑。測試涵蓋 null、檔案不存在、EACCES、stop 失敗、stop 後才有 uri，以及三個呼叫點。
- 麥克風說明：app.json 的 infoPlist 和 expo-audio plugin、languages/ios en 和 zh-Hant、App 內的 denied 文案都已改成「裝置上處理、暫存檔立刻刪除、不儲存不傳送」；prebuild 產生的 Info.plist 也一致。
- audit-ci.json 和 overrides（braces、node-forge、argparse）跟 app3 完全一樣，allowlist 只有 2 筆 GHSA，沒有過度放行。
- README 的 MODIFY_AUDIO_SETTINGS 說明正確（Android 音訊工作階段權限，不是麥克風權限）。
- gitleaks：0 筆；regex（key、token、email、電話、console）：0 筆。
- npm ci OK；jest 45/45（預設時區和 America/New_York）；audit-ci 通過；expo-doctor 18/18；expo prebuild ios OK；git merge-tree 對 main 沒有衝突。

**低風險建議（不擋合併）**
- L1：刪除失敗（例如 EACCES）時會靜默回傳 false，殘檔只會在下次 start 前再試著刪。實務上可以接受，文案寫的「立刻刪除」算是盡力而為。
- L2：`isMissingFileError` 的兩個分支都回傳 false，判斷沒有實際作用，可以之後再簡化。

## R3 重審（head a5d6ed4，增量 b635928...a5d6ed4，2026-10-22）— 結論：通過
- 增量 diff：pr45-r3.diff（13 檔）；乾淨 clone：pr45r3/
- gitleaks 0 筆；regex 新增行無 key/token/email/電話/新 URL/console log
- 無新依賴（package.json/lock 未改）、無網路/分析
- jest 54/54（預設與 America/New_York）、audit-ci 通過、expo-doctor 18/18、prebuild ios 成功、merge-tree 對 main 無衝突
- L1：失敗刪除放入記憶體 Set（同路徑去重），start/stop/unmount 皆先 retryPendingDiscards；不記錄路徑。✔
- L2：isMissingFileError 已移除。✔
- 權限：「再試一次」只在使用者點擊時呼叫 requestRecordingPermissionsAsync，無迴圈；iOS 已拒絕時系統不會再跳窗，改顯示設定提示。✔
- openSettings.js 只呼叫 Linking.openSettings()（App 設定頁），不接受 URL，web 上不丟例外。✔
- 麥克風說明「暫存檔立刻刪除，不儲存、不傳送」與實作一致。✔
- 低（不阻擋）L3：待重試 Set 無上限，若刪除持續失敗每次量測最多 +1 筆路徑，僅在記憶體、App 重啟即清空；可考慮設上限。

## R4 重審（head c2ac448，增量 a5d6ed4...c2ac448，9 檔）— 結論：通過
- L3 已修：PENDING_DISCARD_CAP=20，rememberFailed 以 Set 插入順序丟最舊、重複 URI 不重複加，有界；無 log、不記路徑。
- 停止凍結最後平滑值（freezeMeter），liveRef 阻擋停止後的 tick；max/avg 用平滑值；session 只剩 count/sum/max（O(1)），-160 不重複計數。
- 文案：en/zh-Hant 皆改「not saved / 不會存下來」，EN Offset→Adjust；app.json infoPlist 與 expo-audio microphonePermission 仍寫明「暫存錄音立刻刪除、不儲存不傳送」，與實際行為一致，未宣稱完全不產生檔案。
- 無新依賴、無網路、無 console/log；gitleaks 0、regex 0。
- jest 58/58（預設與 America/New_York）、audit-ci 通過、expo-doctor 18/18、expo prebuild ios 成功、merge-tree 對 main 無衝突。
- 備註（資訊）：短版拒絕文案「不會存下來」不提暫存檔，因系統權限說明已揭露，可接受。
