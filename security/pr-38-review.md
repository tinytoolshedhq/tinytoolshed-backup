# PR #38 安全審查（tinytoolshedhq/app，commit 1cf3f34）
結論：**通過**（附一個與本 PR 無關、需另開 PR 的事項）

## 範圍
- 只改 4 檔：app1/game、app3/mobile 的 package.json（新增 overrides argparse ^2.0.1）與 package-lock.json（+9/-37，只有刪除 argparse 1.0.10、sprintf-js 1.0.3，argparse 提升為 2.0.1）。沒有新增套件。
- 新增/變更的 lock 項目 resolved 皆為 registry.npmjs.org，皆有 sha512 integrity。（apple-foundation-models 是本地 link，main 上原本就有。）
- gitleaks（origin/main..pr38）：no leaks。merge-tree 對 main：無衝突。

## sprintf-js
- 兩個目錄 npm ci 後 node_modules 都沒有 sprintf-js；npm ls sprintf-js 為空。
- argparse 使用者：js-yaml 3.15.x（@istanbuljs/load-nyc-config，jest 覆蓋率用）與 js-yaml 4.x。js-yaml 3 只在 bin/js-yaml.js（CLI）require argparse，函式庫本身不用；實測 require('js-yaml').load 正常。jest 394 全過，覆蓋率路徑不受影響。
- 全部是開發/建置工具，不會打包進 app。

## 測試
- app3 jest：預設時區 394/394、TZ=America/New_York 394/394；完整跑 3 次皆過。
- 421 → 394 的差異：main 目前停在 #35（a88a9da），#37 尚未合併；#37 新增 ai-edit-sheet、reminderSchedule 等測試，所以本分支少了那 27 個。不是測試被刪。
- iap.test.js「ignores purchase-updated events for other products」：單獨跑 10 次 10/10 過；main 上 5/5 過。本地無法重現不穩定；本 PR 沒動 IAP 或 jest 設定，CI 失敗判斷與本 PR 無關（若持續出現，建議另查該測試的 timer/事件順序）。
- expo-doctor 18/18；expo prebuild --platform ios 成功。

## 發現
- **I1（中，與本 PR 無關，既有）**：audit-ci（allowlist braces、node-forge）在 app3/mobile 失敗：uuid 7.0.3 GHSA-w5hq-g745-h8pq（moderate），路徑 expo-sharing → @expo/config-plugins → xcode → uuid，僅 prebuild 用、不打包。main 上同樣失敗 → 是新公告，非本 PR 造成。碼農說本地 audit-ci 過，可能是公告較新。修法：另開 PR，確認是否有修補版後用 overrides 升級 uuid（需驗證 xcode 相容），或暫時 allowlist 並記錄理由。
- **I2（資訊）**：app1/game 有大量既有公告（shell-quote critical、xmldom、undici、tar 等），app1 原本不在審查 audit 範圍；本 PR 讓 app1 少了一個問題，沒有變差。若 app1 還會出版本再處理。
