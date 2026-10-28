# App Store 新功能評估：頁首推廣、搜尋結果自訂、自訂產品頁（2026-10-20）

來源：Harry Ng (@harryworld) 的 Threads 貼文，由 Chun 分享。以下事實都以 Apple 官方資料為準，【推論】是我的判斷。

## 1. 現在能不能用？
- **頁首推廣（Product Page Header）與搜尋結果素材（Search results assets）**：Apple 在 2026-10-05 宣布「Now available」，WWDC26 也有專場介紹。可以上傳圖片或影片，不必是 App 截圖，統一由新的 Asset Library 管理；送審前可以用 App Store Connect 的預覽工具檢查。顯示需要 iOS/iPadOS 27。
  - 頁首：比例 21:9，3840×1646，影片 5–30 秒，30/60fps。
  - 搜尋結果：比例 3:2，1920×1280 到 3840×2560，影片 5–30 秒，預設靜音並循環播放。
  - 素材也能用在 In-App Event 卡片、自訂產品頁、產品頁 A/B 測試（PPO）和 Apple Ads。素材核准後可以直接替換，不必送新版 App。
  - 另外：2027 年 4 月起，新送審的 App 必須附 iPhone Duo 截圖。
- **自訂產品頁（CPP）＋關鍵字**：已可用。每個 App 最多 70 頁，每頁可以設不同的截圖、預覽影片、宣傳文字和 deep link。
  - 只能從「最新已核准版本」的關鍵字中挑選，指派給某個 CPP。CPP 經核准並設為 visible 後，搜尋這些字的人會看到該 CPP，而不是預設頁。
  - 同一組關鍵字只能對應一個頁面。
- **前提條件**：App 至少要在一個地區處於 Ready for Distribution（預購也可以），CPP 要送審，但可以獨立於 App 更新。
  - 【推論】Been Ages 還沒上架，所以現在做不了，上架核准後才能開始。

來源：
- https://developer.apple.com/news/?id=ljpl7kyn
- https://developer.apple.com/app-store/whats-new/
- https://developer.apple.com/videos/play/wwdc2026/205/
- https://developer.apple.com/help/app-store-connect/reference/app-information/creative-assets-specifications/
- https://developer.apple.com/help/app-store-connect/create-custom-product-pages/configure-multiple-product-page-versions/
- https://developer.apple.com/app-store/custom-product-pages/
- https://developer.apple.com/app-store/search/

## 2. 對 Been Ages 值不值得優先做？
【推論】值得，但排在上架之後，屬於零成本、第二週再做的事。理由：
- 新 App 沒有評分，搜尋結果裡的第一張圖就決定點擊率。
- 這些素材不必送新版就能換，適合一人團隊反覆測試。
- 上架前先把素材做好，存進 Asset Library 等用。
- 免費的 PPO 可以拿來 A/B 測試。不使用 Apple Ads，因為要花錢。

### 第一批 CPP 規劃（每頁一組不重複的關鍵字）
| CPP | 市場 | 關鍵字 | 截圖 1 | 截圖 2 | 截圖 3 |
|---|---|---|---|---|---|
| A 上次做是什麼時候 | US/GB | last time, when did, ago, tracker | 列表顯示「12 days ago」等天數 | 單一項目的歷史紀錄 | 分享卡（mint 色） |
| B 已經幾天了 | US/GB | days since, counter, how long | 點一下就記錄、天數歸零 | 自訂分類（家事、保養） | 提醒（多種週期＋延後） |
| C 家事保養 | US/GB | chores, clean, filter, upkeep | 濾網／床單等項目列表 | 提醒設定 | 資料只存在手機、無帳號 |
| D 何日ぶり | JP | 何日ぶり, 前回, 経過, 家事 | 「何日ぶり」天數列表 | 前回の記録（歷史紀錄） | 通知リマインダー |
| E 上次是什麼時候 | TW | 多久, 幾天, 家事, 提醒 | 天數列表 | 歷史紀錄 | 提醒＋分享卡 |

- 避開 JP 競品 Itsu 用的「いつやった／最後にやった」。TW 不要把「上次是什麼時候」當關鍵字，因為這是競品名稱，Apple 禁止用競品名當關鍵字。
- 文案不提 widget、iCloud、鎖定畫面，也不用「unlock」。

## 3. 15–30 秒示範片可行性
- **App Store 的 App 預覽影片**：15–30 秒，iPhone 6.9 吋要 886×1920（直）或 1920×886，最高 30fps，H.264，10–12Mbps，檔案不超過 500MB，每種尺寸每種語言最多 3 支。
  - App Review Guideline 2.3.4 規定預覽只能用 App 本身的畫面錄影。所以「截圖做成動畫」的影片不能當 App 預覽。
  - 做法：用 iPhone 螢幕錄影，再用 CapCut 剪輯，加字幕或裝置外框都可以，零成本，可行。
- **頁首和搜尋結果素材**：可以用品牌圖像，不限 App 內畫面。用截圖加圖示做動畫是允許的，但要換成 21:9 或 3:2 比例、5–30 秒。【推論】一樣要通過審查。
- **社群 Reels**：沒有限制。同一支素材改成 9:16 版本就行。

### 分鏡（20 秒，螢幕錄影）
1. 0–3 秒：列表畫面，字幕「上次換濾網是什麼時候？」
2. 3–7 秒：點一下記錄，天數歸零
3. 7–11 秒：打開項目，看歷史紀錄
4. 11–15 秒：設定提醒（每 30 天、可延後）
5. 15–18 秒：產生分享卡、換顏色
6. 18–20 秒：圖示＋「Tap once. See how long it's been. Pay once.」以及「On-device, no account.」

## 下一步
上架核准後：先送出 CPP A、B、D、E，再上傳 3:2 搜尋素材，接著開 PPO 測試。素材可以現在先錄、先剪好。
