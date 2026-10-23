# PR #46 資安審查（app4 分貝計，head 819c5a1）
結論：**通過**

## 檢查結果
- gitleaks（diff 與整棵樹）：0 筆。regex（key/token/email/電話/EXPO_PUBLIC_/team id/ASC id/appleId）：0 筆。
- eas.json 無 appleId/ascAppId/appleTeamId；app.json projectId 為佔位符 0000…0000。無 .p8/.p12/.mobileprovision/credentials.json。
- Native（AudioMeasurementSessionModule.swift）：只暴露 enableMeasurementMode 一個 AsyncFunction；沿用現有 category（playAndRecord/record）與 options，不新增 allowBluetooth；無檔案寫入、網路、log；錯誤用 do/catch 回傳 false，不會 crash。podspec / expo-module.config.json 正常。
- JS fallback：requireOptionalNativeModule + try/catch，Expo Go 與非 iOS 皆 no-op。
- 麥克風說明 en / zh-Hant / app.json / plugin 一致且符合實作；prebuild 產生的 Info.plist 無 UIBackgroundModes，背景錄音/播放皆 false。
- 新依賴只有本地 file: module。jest 68/68（預設與 America/New_York）、audit-ci 通過、expo-doctor 18/18、prebuild ios 成功且模組 autolink、merge-tree 無衝突。
- bundle id com.decibelmeter.app：請確認在 Apple 帳號可註冊（僅備註）。

## 低風險建議（不擋合併）
- L1（低）app4/mobile/.gitignore：已含 *.p8、*.p12、*.mobileprovision、.env，但缺 credentials.json，建議補上。
- L2（低）Swift 模組停止量測時不呼叫 setActive(false)，目前交給 expo-audio 管理 session；建議實機確認停止後其他 app 音訊能恢復（README 也寫尚未實機驗證）。
