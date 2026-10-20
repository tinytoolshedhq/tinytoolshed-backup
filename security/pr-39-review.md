# PR #39 安全審查（app3 uuid GHSA-w5hq-g745-h8pq）— 6153028
結論：通過

- 作法：npm overrides（非 allowlist），package.json:54 `"uuid": "11.1.1"`；lock 指向 registry.npmjs.org，含 sha512 integrity（vIYx…ZgQ==）。lock 內只有一個 uuid（xcode 依賴鏈），無其他使用者被影響。
- 相容性：uuid 11 仍提供 CJS，`require('uuid').v4` 正常；xcode/lib/pbxProject.js:22,90 只用 `uuid.v4()`，無 deep import。實測 xcode 解析 prebuild 產生的 project.pbxproj 並 addPbxGroup 產生 UUID 成功。
- gitleaks（main..pr39）：無外洩。npm ci 成功。
- audit-ci（braces、node-forge）：GHSA-w5hq 已消失；仍擋 sprintf-js GHSA-hp3w-g68c-fv3c，為 main 既有、由 PR #38 修正，與本 PR 無關（暫 allowlist 後通過）。
- jest 預設時區及 America/New_York：28 suites / 394 測試全過（本地 IAP 測試未失敗）。
- expo-doctor 18/18；`expo prebuild --platform ios --clean` 成功，pbxproj 格式有效。
- merge-tree vs main：無衝突。
- 低風險備註：#38 與 #39 都改 app3 package.json overrides／lock，後合併者需 rebase 重產 lock。
