# PR #52 審查（Been Ages IAP 修正）— head 51bb23f
結論：**通過**（附低風險建議，不擋合併）

已知低風險項（1 個 L1、1 個 L2），追蹤中，修正合併後補完整內容。

## 3. finishTransaction / E_ALREADY_OWNED — 通過
- finish 在 verify 後無條件呼叫、錯誤吞掉（:187-192、:201），不會留 pending；一次性非消耗品先 finish 無害。
- pending/revoked/不符 productId 的交易不 finish（:196-197），屬正常（由 StoreKit 重送）。
- E_ALREADY_OWNED：requestPurchase throw（:369）、error listener（:296、:388）、外層（:417）皆走 tryNativeRestore ✔

## 4. 秘密外洩 — 無
- diff 無 key/token/secret/email/console.log；錯誤訊息只顯示 error.message（:304），不含收據/JWS/交易 id。

## 5. Chun checklist
- podspec：PR 未改；AppleFoundationModels.podspec 無 __dirname/require/module.exports。box 無 ruby，未跑 ruby -c（#48 的 CI 已覆蓋）。
- app.json 有 NSPhotoLibraryUsageDescription＋AddUsageDescription，languages/ios/ 5 語系皆有 ✔
- ios.buildNumber = 12（未改；ASC 最高 12，autoIncrement 下一版 13）✔

## 6. 測試
- npm ci 成功；jest 509/509（預設時區、America/New_York）
- expo-doctor 20/21：套件版本與 SDK 不符（PR 未改 package.json，既有問題）
- git merge-tree vs origin/main：無衝突

## 7. 文案
- 只新增 iap.restored 五語系字串，未動隱私權政策/商店說明。
