# backup PR #3 安全／隱私審查（tinytoolshedhq/tinytoolshed-backup）

- 日期：2026-10-20（台北時間）
- 來源：/workspace/security/backup-pr3-files.tar.gz → /workspace/security/pr3/（未使用 GitHub 連線或任何帳號，唯讀）
- 結論：**通過**

## 檢查項目
- gitleaks 8.21.2 `dir`：no leaks found
- 文字 grep（email、token、key、team ID、ASC ID、Apple ID、電話、UDID、10 碼 ID）：無命中；只出現 commit hash a88a9da、f737573 與程式檔路徑
- 22 張 PNG（皆 780×1688）：沒有 EXIF、GPS 或 PNG 文字欄位
- 22 張截圖逐一檢視：都是 Expo web 的 app 畫面，沒有狀態列、電信商、通知橫幅、裝置名稱、TestFlight、帳號、email、位置或其他 app 內容。資料都是測試用假資料（澆花、換牙刷、打給媽媽、幫貓剪指甲等），沒有真實姓名。付費頁顯示「無法取得價格」，沒有帳號資訊

## 發現
- I1（資訊，不需修正）：test-run 檔寫到共用電腦的內部路徑 `/workspace/bv`，不算敏感
- I2（資訊）：壓縮檔裡沒有 README，「每次 build 前都要跑一次 test-flows.md 的全部流程」這一行是依碼農的說明審的，文字本身沒有風險
