# PR #52 審查（Been Ages IAP 修正）— head 51bb23f
結論：**通過**（附低風險建議，不擋合併）

## 1. 未驗證交易能否解鎖 — 低
- src/lib/iap.js:194-213 grantFullpackPurchase：verify 結果被忽略（:200），finish 後先重讀 entitlements（:203），若沒有則 :205-209 直接信任 purchase 事件 payload 並寫入持久 setProUnlocked(true)。
- payload 來自原生 StoreKit purchaseUpdatedListener / requestPurchase 回傳值（:224、:379），非網路輸入；偽造需越獄/hook，本地買斷 app 可接受。且啟動時 verifyProOnLaunch（:532-563）以 entitlements 為準，連續 3 次成功但無 Full Pack 會鎖回，故錯誤解鎖最終會被校正。
- productId 比對嚴格相等（:60-67），不接受任意 productId；pending/revoked 被排除（:83-85）。
- 建議：:207 fallback 前延遲重讀 entitlements 1–2 次（例如 1s/3s）；或僅在 verify===true 時才持久化，否則只在本次 session 解鎖。
- 注意 PRO_PRODUCT_ID 可被 EXPO_PUBLIC_IAP_PRODUCT_ID 覆寫（:10-11），production 不應設定。

## 2. 撤銷/退款 — 低
- 讀取失敗/離線（ok:false 或 throw）不累加、不撤銷（:157-175、:542、:560）✔
- 成功但無 Full Pack：累加 streak，3 次後撤銷（:91-112）✔ 不會因錯誤誤撤銷。
- 建議：若 entitlement 清單中明確出現 Full Pack 且帶 revocationDate（退款），應立即撤銷，不必等 3 次。

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
