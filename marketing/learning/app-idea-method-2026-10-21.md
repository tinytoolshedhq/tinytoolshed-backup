# 新 App 主題發想方法論 + 候選主題（2026-10-21）
資料來源：iTunes Search API（https://itunes.apple.com/search?term=...&country=us|jp&entity=software），2026-10-21 查詢。
限制：API 不回傳 IAP 價格/下載量；「付費意願」以 免費+IAP 模式下的高評分數推論【推論】。IAP 價格需到商店頁確認【未查證】。
Reddit/X/Product Hunt/Google Trends/Sensor Tower 本輪未查【待補】。

## 一、流程
1. 發想來源：App Store 工具類排行、搜尋建議、Reddit「is there an app that」、X「I'd pay for an app」、Product Hunt。
2. 硬條件篩選：免登入、可純裝置端、Expo 可做、非 Been Ages 同類、不需伺服器。
3. 競品 3 個（現可下載）：記錄 id、價格/IAP、評分數、平均分、最近更新、優勢、負評痛點。
4. 好打廣告：主關鍵字在 us/jp 搜尋有 ≥5 個相關 app、搜尋建議會出現該詞、名稱可放關鍵字。
5. 付費意願門檻：頭部競品 ≥1,000 評分（US）且有付費版/IAP；至少 1 個競品近 6 個月有更新；平均 ≥4.3。
6. 缺口：頭部是否老舊（>2 年未更新）、訂閱制被罵、廣告過多 → 我們打「一次買斷、無廣告、無帳號」。
7. 評分（各 1–5）：需求、付費證據、關鍵字清晰度、競爭可打性、開發成本（越低越高）、JP 機會。總分 30，≥21 才提案。
8. 淘汰條件：需登入/伺服器；頭部 >100 萬評分且由大廠把持；無付費證據；與 Been Ages 重疊；需付費 API。

## 二、候選主題
### 1. 間歇訓練計時器（Interval/HIIT Timer）— 24/30
關鍵字：interval timer, hiit timer, tabata timer / インターバルタイマー, HIITタイマー
- Interval Timer □ HIIT Timer (1124297113) 免費+IAP，US 87,120 評分 4.8，JP 4,563；優勢：預設模板、Apple Watch。
- Timer Plus (1279716547) 免費+IAP，JP 62,124 評分 4.7；優勢：JP 在地化強。
- Intervals Pro (957586938) 免費+IAP，US 13,693 評分 4.8；優勢：自訂多段。
- 缺口：多為訂閱【推論】；我們：一次買斷、語音提示 ja/en、極簡。
### 2. 噪音/分貝計（Decibel Meter）— 22/30
關鍵字：decibel meter, sound meter, noise meter / 騒音計, デシベル
- Decibel X (448155923) US 163,236 評分 4.6、JP 19,259；優勢：校準、報表。
- Decibel Meter Sound Detector (1254994873) US 55,666 4.7（2025-05 後未更新）。
- NIOSH SLM (1096545820) US 16,909 4.7；免費政府權威。
- 缺口：JP 頭部僅 4.2–4.3 分；我們：鄰居噪音紀錄匯出（裝置端）。
### 3. 計數器（Tally Counter）— 22/30
關鍵字：tally counter, click counter / カウンター, 数取り
- Counter Tally Count (1144352844) US 14,001 4.8。
- Count That Now (955952873) US 5,484 4.7（2024-09 後未更新）。
- カウンター 読み上げ (1524807764) JP 5,896 4.4。
- 缺口：開發成本極低、JP 需求明顯；風險：付費意願較弱【推論】。
### 4. 節拍器（Metronome）— 21/30
關鍵字：metronome, tempo / メトロノーム
- Smart Metronome & Tuner (889571826) US 61,660、JP 146,859。
- Soundbrenner (1048954353) US 48,371 4.7。
- Pro Metronome (477960671) US 20,570 4.7。
- 缺口：JP 需求極大；需低延遲音訊，Expo 可行性待驗【未查證】。
### 淘汰：白噪音、PDF 掃描、單位換算、分帳（頭部百萬級或需同步/帳號）。

## 三、補充資料（2026-10-21 第二輪）
**GB 評分數**（iTunes API country=gb）：Interval Timer HIIT 44,137／Decibel X 22,164、Decibel Meter 8,956／Count That Now 1,816、Counter Tally 1,468、Tasbih Counter Pro (1341100401) 4,551／Metronome Ϟ 9,700、Soundbrenner 9,149、Smart Metronome 3,885。
**搜尋建議**：MZSearchHints 回傳空清單（端點已失效），改由搜尋結果數量推估【推論】。
**IAP 價格**（apps.apple.com/us 頁面抓取的 $ 金額，未對應到方案名稱【部分未查證】）：
- Interval Timer HIIT 1124297113：$1.99–$34.99（推測含年訂）
- Timer Plus 1279716547：$2.99–$34.99
- Decibel X 448155923：$1.99–$69.99（高價年訂/買斷）
- Counter Tally 1144352844：$19.99
- Smart Metronome 889571826：$4.99／$7.99／$40.99
- Pro Metronome 477960671：$0.99–$40.99
- Seconds 475816966：一次付費解鎖，評論稱讚「不是訂閱」（https://apps.apple.com/us/app/seconds-interval-timer/id475816966）
**Reddit/網路**：間歇計時器已有多個獨立開發者的一次買斷新品：Tockr £0.99（https://www.reddit.com/r/iosapps/comments/1s47j1l/）、SeqTimer $1.99（https://tansfom.com/SeqTimer/press.html）→ 「買斷」差異化變弱。
**X**（search_posts_all）：相關貼文很少；只看到計數器「無廣告、無訂閱」需求（https://x.com/quitedev357/status/2108844214717173937，Android）、notch 計數器宣傳（https://x.com/schnell7labs/status/2102641936448573664）。訊號弱。
**Google Trends / Product Hunt**：本輪未抓取（Trends 需瀏覽器）【待補】。

## 四、重新評分
1. 分貝計 23/30（↑1）：頭部年訂 $49.99–69.99，一次買斷 $2.99 有價差；JP 評分偏低。→ 第一優先
2. 間歇計時器 21/30（↓3）：需求最大，但獨立開發者的買斷產品已擠入。
3. 節拍器 21/30（持平）：$40.99 高價方案證明付費意願；Expo 低延遲音訊仍是風險。
4. 計數器 21/30（↓1）：Counter $19.99 證明有人付費；可延伸 Tasbih／念珠計數小眾（GB 4,551 則評分）。
