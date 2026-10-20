# 蘋果大師（apple-master）

Chun 的 iOS 上架負責人：EAS build、TestFlight、App Store Connect 送審（含內購）、截圖、metadata、隱私標籤、審核回覆。
- 程式修改 → 可憐的碼農；安全審查 → 漏洞大師；協調 → 黑嘛嘛。

## 目前狀態（2026-10-20 台北時間）

### App：Been Ages／好久沒了
- Repo：ChunWang1998/app，資料夾 `app3/mobile`；Expo SDK 57
- EAS：帳號 leowang1105，專案 @leowang1105/been-ages（33ece313-8cae-4778-8ec5-e483fc9bf204）
- Bundle：com.beenages.app；Team：JXJL44F45W
- ASC Apple ID 6822311922，SKU beenages-ios
- 內購：com.beenages.app.fullpack（Apple ID 6822312264，非消耗型，expo-iap）
  - 首發價 US$2.99 / £2.99 / ¥480；預計上架約 21 天後（約 2026-11-09）改為 US$3.99 / £3.99
- TestFlight 群組 Internal（efcf487a-38d2-4643-ac99-cf2ed1dd8f51）
- 隱私權：https://chunwang1998.github.io/app/app3/store/privacy.html；支援：同資料夾 support.html
- App Privacy：Data Not Collected；分類 Productivity / Lifestyle；免費 app

### Build 歷史
| Build | 版本 | 來源 | 結果 |
|---|---|---|---|
| 3 | — | — | 暫用 icon |
| 4 | 1.0 | — | 已送審，經 Chun 同意撤回 |
| 5 | — | — | 被退：ITMS-90683 缺 NSCalendarsUsageDescription |
| 7 | 1.1.0 | a80902d | 2026-10-14 10:08 與 Full Pack 一起送審（review submission 6dca7e50） |
| 8 | 1.1.1 | 0221d9c | 10/17，TestFlight |
| 9 | 1.1.1 | d3a510c（AI 輸入） | 10/20 被退：ITMS-90683 缺 NSPhotoLibraryUsageDescription |
| 11 | 1.1.1 | f737573 | EAS bd014584-fd45-4ae9-9fbb-6fad97439762，ASC build 3a47b665-86fc-4b5e-81b7-0e52f279ac38，VALID，Internal IN_BETA_TESTING |

註：main 的 buildNumber 是 10，autoIncrement 讓它變成 11。

### 2026 年 10 月 build 額度
15 次用了 9 次，剩 6 次（EAS 免費方案）。

### 審核狀態
- 1.1.0、Full Pack 內購、submission 6dca7e50：皆 WAITING_FOR_REVIEW（2026-10-20 查）
- 每日排程「Been Ages 審核狀態追蹤」09:04（台北）檢查；有結果或過了 2026-11-14 後自刪。

### 待辦
- 核准後：排定正式價格；視需要建立 Offer Codes。
- 1.1.1 商店 metadata（en-US / zh-Hant / ja / en-GB；拿掉小工具；免費上限 10 項 × 每項 10 筆；What's New 註明移除小工具）和新截圖需重做——/workspace/beenages-store 的草稿在 10/20 box 重設時遺失。等 1.1.0 審完且有明確指示才上傳。
- 1.1.1 本身尚未送審。
