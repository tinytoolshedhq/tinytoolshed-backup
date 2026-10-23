# PR #47 資安審查（app4 分貝計，head f90fc4b）
結論：**通過**（附 2 個低風險建議）

## 檢查
- gitleaks（diff + 整個 app4/mobile）：0 筆；regex（key/token/email/電話/EXPO_PUBLIC_/appleId/ascAppId/teamId）：0 筆；eas.json 無 Apple/ASC/team 欄位。
- projectId `117e…debcb` 為 UUID；owner `leowang1105` 是 Expo 帳號名（公開識別碼）。看起來像個人帳號而非品牌帳號（未查詢任何服務）；若未來要轉品牌，建議由蘋果大師評估改用 Expo organization。
- jest：71/71（預設與 America/New_York）；audit-ci 通過；expo-doctor 18/18；expo prebuild ios/android 成功；merge-tree 對 main 無衝突。

## 相簿權限
- app 本身沒有使用相簿（無 expo-media-library / image-picker / 截圖分享）。
- 來源：expo-file-system `ios/Legacy/FileSystemHelpers.swift` 引用 `PHPhotoLibrary.authorizationStatus`，二進位含此 API 會觸發 Apple ITMS-90683，所以必須有字串。
- 文案誠實寫明「不會使用照片／系統元件需要」，中英一致，prebuild 的 Info.plist 正確。執行時不會跳出相簿權限要求，App 隱私標籤不需勾選照片。可接受。

## Native restoreSession
- 第一次 enable 時保存 category/mode/options，stop 時還原後清空，再 `setActive(false, options: .notifyOthersOnDeactivation)`；所有錯誤皆 catch，回傳 Bool；JS 端再包 try/catch。無 log、檔案、網路。
- 執行緒：AsyncFunction 在 Expo 模組佇列執行，AVAudioSession 可在背景執行緒呼叫，OK。

## 低風險建議
- L1：`android.permissions` 只是「加入」，不會移除預設權限。prebuild 後 AndroidManifest 仍有 INTERNET、READ/WRITE_EXTERNAL_STORAGE、SYSTEM_ALERT_WINDOW、VIBRATE。PR 說「Android 只留兩個」不成立。目前不出 Android 版所以不擋；若要成立需加 `android.blockedPermissions`。
- L2：restoreSession 在沒有 snapshot 時也會 setActive(false)，可能與 expo-audio 的狀態不同步；請阿姨在實機確認「停止→再開始」正常。
