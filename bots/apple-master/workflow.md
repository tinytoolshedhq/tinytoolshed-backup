# 工作流程（蘋果大師）

## Build / 上傳 / 送審
1. PR 由漏洞大師審過並合併。
2. 重新 clone main（不用舊的本機修改）。
3. 本機驗證：
   - `npx expo-doctor`
   - 乾淨的 `npx expo prebuild -p ios --clean`
   - `npx expo export`
   - Info.plist 用途說明（含各語系 InfoPlist.strings）
   - 掃描原生程式碼中需要用途說明的隱私 API，避免 ITMS-90683
   - entitlements、版本號 / build 號、credentials
4. 向黑嘛嘛回報內容與剩餘 build 次數，等 Chun 同意。
5. `EXPO_NO_CAPABILITY_SYNC=1 eas build -p ios --profile production --non-interactive`
   - 失敗不重試；把日誌重點送給黑嘛嘛和碼農。
6. `eas submit -p ios --id <id> --non-interactive`
   - eas submit 會忽略環境變數，所以暫時把 ASC 欄位加進 eas.json，完成後 `git checkout eas.json`，絕不 commit。
7. 輪詢 ASC 直到 VALID；查 Gmail 有無 ITMS 退件信。
8. 加進 Internal 群組，填 What to Test。
9. 只有明確指示才送審。第一個內購必須在 ASC 網頁加到版本；App Privacy 也只能在網頁設定。

## 金鑰與憑證（不含任何機密內容）
- **EXPO_TOKEN**：box 上的環境變數（值不寫在任何地方）。
- **ASC API 金鑰**：Key ID 84374CR3FZ，Issuer 756fe3f0-2649-4ab1-a0c6-93ba3e80c976
  - .p8 位置：`/home/box/.secrets/asc/AuthKey_84374CR3FZ.p8`，同資料夾有 meta.json 和 asc.py 輔助腳本（資料夾 700、檔案 600）。
  - 舊金鑰 4KH7HCWT4D 在 box 重設時遺失（EAS 上可能仍存有）。
- **簽章**：distribution cert 由 EAS 管理；profile L7A5XCN8C8（app）有效至 2027-08-05；舊小工具 profile Y67JMWRCC8 已不使用。

### 金鑰遺失時重建
1. Account Holder / Admin 到 App Store Connect → Users and Access → Integrations → App Store Connect API。
2. 建立新金鑰（權限 App Manager 或 Admin）。
3. 下載 .p8（只能下載一次）。
4. 複製到 `/home/box/.secrets/asc/`，更新 meta.json。
5. 視需要更新 EAS credentials。
- 建議把 .p8 離線備份在密碼管理器。
