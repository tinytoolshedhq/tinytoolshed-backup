> [RESTORED 2026-10-20] 歐洲小編復原：原版（2026-10-14／17）逐字復原；ASO 修訂版依 2026-10-17 寫入內容復原，並套用 2026-10-20 的更新（keywords 改 oven、contacts；app 1.1.1 免費版依 Chun 2026-10-20 定案維持 10 個項目＋每項 10 筆紀錄、widget 已移除）。行銷大師 2026-10-20 重建版附在最下方。

# Been Ages — 英國：搭美國順風車的 ASO 版（草稿，需 Chun 核准）

- 整理：2026-10-14（台北時間）；2026-10-17 更新：美國計畫已拿掉 Reddit，英國仍只靠美國 PH／X／英文媒體順帶覆蓋。
- **2026-10-17 Chun 決定：英國不發社群貼文、不回覆，只做 ASO。** `../social/drafts/GB/posts.md` 已擱置。
- 定位【推論】：英國不另做社群主動出擊，只做在地化 ASO；Product Hunt、X、英文媒體由美國計畫順帶覆蓋（同語言、全球可見）。
- 理由：【證據】英國沒查到買斷制零成本在地案例；查到的英國成功案例（Mumigo 520 萬下載、Personal Best）都主要靠 ASO（`../learning/by-country/GB.md`，https://rosetta.to/u/starterstory/how-i-built-a-30k-month-mobile-app ）。Ofcom 只有未成年平台數據（YouTube／TikTok 為主），X/Threads 帶量有限。
- 規則同美國版：零成本、每則要 Chun 核准、不自動留言、不開分身。

## ASO（en-GB）修訂版 — DRAFT, needs Chun approval

- 修訂：2026-10-17，2026-10-20 更新（台北時間）｜歐洲小編。依據 `../social/phrase-bank/GB.md`、`been-ages-us-outreach.md` §4、app 現有功能（`/workspace/bv/app3/mobile/README.md`、`languages/en.json`）。
- 檢查腳本：`../scripts/check-aso.py`（三語）／`../scripts/check-aso-gb.py`（同一支，預設只查 gb）。

### 欄位
| 欄位 | 內容 | 長度／上限 |
|---|---|---|
| Name | Been Ages: Last Time Tracker | 28／30 |
| Subtitle | Days since chores, MOT & more | 29／30 |
| Keywords | reminder,habit,routine,oven,boiler,service,toothbrush,kettle,bedding,contacts,clean,radiator,descale | 100 bytes／100 |
| Promotional text | When did you last descale the kettle, change the bedding or book the boiler service? Tap once when it's done and Been Ages counts the days. Pay once, no subscription. | 166／170 |

- Subtitle：美國版「Days since you last did it」的 *last* 和名稱重複，改成「Days since chores, MOT & more」。
- Keywords（2026-10-20 依行銷大師建議）：log → **oven**、lenses → **contacts**；為了守住 100 bytes，cleaning → **clean**（另一個選項：保留 cleaning、拿掉 habit）。三欄無重複字。

### Description（1580 字元／4000）
> Been Ages remembers the jobs you only do every so often, so you don't have to.
>
> Changed the bedding? Descaled the kettle? Swapped your toothbrush head? Tap once and Been Ages saves the date. Open it later and you'll see exactly how long it's been: 1 month 17 days, not "about a month".
>
> WHAT YOU GET
> • Log it in one tap. No forms, no faff.
> • The exact time since, in months and days. Never rounded off.
> • A reminder when it's due: weekly, every fortnight, monthly, yearly or any interval you like. Miss one and it nudges you again 3 days later.
> • Overdue items stand out, so you can see what's slipped.
> • Full history, notes and simple stats for every item: how often, on average, and the longest gap.
> • Add the next due date to your Calendar.
> • Share a card when you've finally done it.
> • Light or dark mode.
> • Deleted something by mistake? Undo it, or find it in Recently Deleted for 30 days.
>
> IDEAS TO START WITH
> Boiler service, MOT, car tax, dentist check-up, contact lenses, toothbrush head, bedding, descaling the kettle, bleeding the radiators, defrosting the freezer, cleaning the oven, the cat's flea treatment, or simply the last time you rang your nan.
>
> PRIVATE BY DESIGN
> No account and no sign-up. Your data stays on your iPhone, and we can't see what you log.
>
> PAY ONCE
> Free to download, with up to 10 items and 10 records per item. A one-off purchase gives you unlimited items and extra share card styles. No subscription. Already bought it? You can restore your purchase at any time.
>
> Made by one developer at Tiny Toolshed. Feedback is always welcome.

### 截圖文案（前 3 張講好處；需用英文介面重拍）
| 順序 | 建議畫面 | 文案 | 字元 | 備註 |
|---|---|---|---|---|
| 1 | 清單頁（多個項目＋天數） | Know how long it's been since anything | 38 | 好處 |
| 2 | 單一項目詳情（幾個月幾天） | Exact months and days, never rounded off | 40 | 好處 |
| 3 | 提醒設定 | A nudge when it's due again | 27 | 好處 |
| 4 | 新增／編輯 | Log it in one tap. No faff. | 27 |  |
| 5 | 設定頁「資料」區或隱私說明 | No account. Your data stays on your phone. | 42 |  |
| 6 | 買斷頁 | Pay once. No subscription. | 26 |  |
| 7 | 深色模式畫面 | Light or dark, your call | 24 |  |

- 舊截圖是繁中介面，不能用。app 1.1.1 已移除 widget，買斷頁不再有 widget 字樣（2026-10-20 查 `languages/en.json`）。
- 範例項目用英國情境：Boiler service、MOT、Descale the kettle、Change the bedding、Toothbrush head【推論】。

### 檢查結果
```
== gb
  name            28 chars    28 bytes  limit 30 chars  OK
  subtitle        29 chars    29 bytes  limit 30 chars  OK
  keywords       100 chars   100 bytes  limit 100 bytes  OK
  promo          166 chars   166 bytes  limit 170 chars  OK
  description   1580 chars  1598 bytes  limit 4000 chars  OK
  caption 1     38 chars  Know how long it's been since anything
  caption 2     40 chars  Exact months and days, never rounded off
  caption 3     27 chars  A nudge when it's due again
  caption 4     27 chars  Log it in one tap. No faff.
  caption 5     42 chars  No account. Your data stays on your phone.
  caption 6     26 chars  Pay once. No subscription.
  caption 7     24 chars  Light or dark, your call
  name∩subtitle      none
  name∩keywords      none
  subtitle∩keywords  none
  keyword repeats    none
  spaces in keywords: False
  plural overlaps: none
  banned words: none
  US spellings: none
  RESULT: PASS
```

### 待 Chun 決定（ASO）
1. 各欄位是否同意。
2. 英國定價：£2.99 一次性購買，無上市優惠，免費 10 個項目（每項 10 筆紀錄），不開家人共享（Chun 2026-10-20 定案：等同 US $2.99 的價格點；MetaRun 2026-10-12 由 App Store Connect API 取得的對照表：GB £2.99、DE €2.99、FR €2.99，上架前請在 ASC 再確認）（說明文不寫價格）。
3. 英文截圖重拍。
4. 要不要加 en-GB app 內文字（Every 2 weeks → Fortnightly）。

### 原版 ASO（2026-10-14，逐字復原）
| 欄位 | 內容 | 長度 |
|---|---|---|
| Name | Been Ages: Last Time Tracker | 28 |
| Subtitle | Days since you last did it | 26 |
| Keywords（100 bytes） | reminder,habit,chores,routine,log,days,since,replace,toothbrush,filter,mot,boiler,service,cleaning | 98 |
- 英式拼字（organise、colour）；截圖範例換成 MOT、boiler service、換牙刷【推論，MOT／boiler 例子未查證搜尋量】。
- 價格：£2.99 一次性購買，無上市優惠，免費 10 個項目（每項 10 筆紀錄），不開家人共享（Chun 2026-10-20 定案：等同 US $2.99 的價格點；MetaRun 2026-10-12 由 App Store Connect API 取得的對照表：GB £2.99、DE €2.99、FR €2.99，上架前請在 ASC 再確認）（一次性購買）。

## D0–D14
| 天 | 行動 |
|---|---|
| D0 | en-GB 商店頁上架（和美國同日） |
| D1–D14 | 不另外發文、不回覆（Chun 2026-10-17 確認：英國只做 ASO）；美國 Product Hunt／X／英文媒體自然覆蓋英國用戶 |
| D14 | 看英國區曝光、下載、搜尋詞，決定是否加碼 |

## 待 Chun 決定
- （已定案：等同 US $2.99 的價格級距，無上市優惠，Chun 2026-10-17/20）
- ASO 修訂版是否同意。

---

Reddit: dropped 2026-10-17 with US plan, revisit later

---
## 行銷大師 2026-10-20 重建版（原樣保留）
> Rebuilt 2026-10-20 after data loss; sections marked [RECONSTRUCTED-PARTIAL] may be incomplete
> 來源：行銷大師記憶摘要（原檔、備份、對話紀錄皆無法取得）。未標註來源者為記憶事實，非新推論。

# Been Ages — GB (ASO only)
（原為歐洲小編修訂版；以下 ASO 欄位已由行銷大師核對過長度與無重複，屬完整復原。）
GB（United Kingdom）不發文，只做 ASO（Chun 決定）。

## ASO
- Name: Been Ages: Last Time Tracker (28)
- Subtitle: Days since chores, MOT & more (29)
- Keywords (100 bytes): reminder,habit,routine,log,boiler,service,toothbrush,kettle,bedding,lenses,cleaning,radiator,descale

## 待議建議（行銷大師→歐洲小編）
- "log" 換成 "fridge" 或 "oven"
- 可考慮 "lenses" 換成 "contacts"

## 價格
£2.99 一次性購買，無上市優惠，免費 10 個項目（每項 10 筆紀錄），不開家人共享（Chun 2026-10-20 定案：等同 US $2.99 的價格點；MetaRun 2026-10-12 由 App Store Connect API 取得的對照表：GB £2.99、DE €2.99、FR €2.99，上架前請在 ASC 再確認）

TODO [RECONSTRUCTED-PARTIAL]: 原檔其他段落請歐洲小編補回。scripts/check-aso-gb.py 不存在。

## 產品功能（開發確認 2026-10-20，main d3a510c）
- 有：提醒（每 N 天／週／月／年、固定星期幾、每月固定日、自訂時間、稍後提醒、匯出到行事曆）；資料只在裝置上（無帳號、無伺服器、無追蹤）；付費頁可恢復購買；中／英／日，跟隨系統語言；自訂分類；每個項目的歷史紀錄；手動匯出／匯入備份檔。
- 沒有（不得宣稱）：widget、鎖定畫面記錄、iCloud 同步、照片備註、時間軸。
- AI 輸入（打字或語音新增、問「多久沒…」、記「剛做完」、復原；完全裝置端、離線）：只能標「Coming soon／即將推出」。
- 免費額度：10 個項目、每項 10 筆紀錄（Chun 2026-10-20 定案，與程式碼一致）。

## Keyword update（2026-10-20 提案，未改上方現行欄位）
依免費代理指標（App Store 搜尋建議＋iTunes Search API，非 Apple popularity 分數），提案見 `learning/keyword-demand-2026-10-20.md` 的「建議」表中 GB 一列。待 Chun 確認後才替換。
