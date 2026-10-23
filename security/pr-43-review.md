# PR #43 資安/隱私審查（head f5479f3）
結論：**需修正**

## 檢查結果
- gitleaks（pr43.diff）：0 筆；新增行 regex（key/token/email/電話/EXPO_PUBLIC_）：0 筆（只有測試字串 'Secret item'）
- 無新套件、無新網路呼叫、無新 log
- jest 503/503（預設時區、America/New_York 皆過）；audit-ci 通過
- expo-doctor 17/18：expo/expo-calendar/expo-sharing 有 patch 版本差異（上游新版，非本 PR 造成，本 PR 未改 package.json）
- git merge-tree vs main：無衝突
- 舊欄位：prefs 不再讀 showNameInNotifications；notificationTitle 不讀 prefs；存留舊值 false 不會報錯（有測試覆蓋）。程式碼中已無 showNameInNotifications / notifyWithName（只剩測試中的 negative assert）。5 語系 notifyWithName 皆已移除。

## 發現
### M1（中）隱私頁仍承諾通知預設不含名稱
- 位置：app3/store/privacy.html 第 39 行（線上頁面同樣內容）
- 內容：「預設通知標題為通用名稱，不含項目名稱；可在設定中開啟『通知含名稱』。」與新行為相反，且指向已刪除的設定。
- 修正：改為「通知標題會顯示項目名稱。若不想在鎖定畫面顯示，可到 iPhone『設定 > 通知 > Been Ages > 顯示預覽』調整。」並加測試（privacy-v11.test.js）禁止「通知含名稱」「不含項目名稱」。EN/JA/DE/FR 段落未提此開關，但建議同步加一句「通知標題包含項目名稱」，與行事曆段落一致。
- App Store 隱私標示不受影響（資料仍只在本機）。

### L1（低）鎖定畫面曝光
- 項目名稱現在一律出現在通知，可能在鎖定畫面被旁人看到。使用者唯一控制是 iOS 系統的「顯示預覽」設定或關閉該項提醒。建議隱私頁/支援頁說明此方法。
