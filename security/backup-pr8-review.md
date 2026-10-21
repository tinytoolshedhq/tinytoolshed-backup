# backup PR #8（每日備份，head c9636e3）安全／隱私審查

- 日期：2026-10-20（台北時間）
- 來源：/workspace/security/backup-daily-2100.tar.gz → /workspace/security/pr8/、backup-daily-2100.diff（純文字 diff -ruN，9 個 md 檔，無刪除）
- 未使用 GitHub 連線或任何帳號，唯讀
- 結論：**通過**

## 檢查結果
- gitleaks（/tmp/gitleaks dir）：no leaks found
- 文字 regex（token、secret、key、team ID、ASC ID、issuer、Apple ID、UDID、email、電話、32 碼以上 hex、sha512- integrity、10 碼 ID）：無命中
  - 只出現 commit hash、程式路徑、npm 套件名稱（@istanbuljs 等）、GHSA 編號
- 安全審查報告（pr-3、35、37、38、39）：沒有任何完整密鑰；pr-38 只寫「皆有 sha512 integrity」，沒有引用 hash 本身
- reply-log/asia-submitted.md：只有 3 輪、共 28 個 X 公開貼文連結（含公開帳號名稱），沒有姓名、email、私訊內容或其他私人資訊
- 圖片 metadata：92 張 PNG 和 1 個 GIF 都沒有 EXIF、GPS 或 PNG 文字欄位
- 92 張 PNG 全部用縮圖拼圖檢視過（user-tester 70 張、bugs-real 22 張）
  - 都是 Expo web 的 app 畫面（首頁、編輯、AI 聊天、付費頁、設定、提醒、最近刪除）
  - 沒有狀態列、電信商、通知橫幅、裝置名稱、TestFlight 或帳號、email、位置或其他 app 內容
  - 資料都是測試用假資料
  - 設定頁版本號為 Been Ages 1.1.1
- GIF demo-real-1.5x.gif（340×737，285 幀）：平均抽 8 幀檢查
  - 片頭是「網頁版僅規則解析 / PR #30 AI 輸入 · main f737573」，其餘都是 app 畫面
  - 沒有個資

## 發現
- I1（資訊，非隱私問題）：pr38/18-privacy.png 拍到 GitHub Pages 404。這是 PR #38 測試當時隱私權連結打不開，跟本 PR 的安全性無關；建議確認 tinytoolshedhq 的隱私權頁目前可以連上
- I2（資訊）：reply-log 列了第三方的 X 帳號名稱，但都是公開貼文連結。repo 是私有的，可以接受
