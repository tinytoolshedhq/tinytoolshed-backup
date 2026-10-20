# Been Ages 關鍵字需求估算（2026-10-20）

> **全部是代理指標／估算，不是 Apple Search Ads 的 popularity 分數（1–100）。** Apple Ads 需要付款資料又選不到未上架 app，已停用（蘋果大師 2026-10-20）。
> 抓取時間：2026-10-20 17:53–17:55（台北時間）。腳本與原始資料：`/workspace/kw/run.py`、`/workspace/kw/out.json`。

## 方法
1. **App Store 搜尋建議**：`https://search.itunes.apple.com/WebObjects/MZSearchHints.woa/wa/hints?clientApplication=Software&term=<prefix>`，header `X-Apple-Store-Front: <id>-1,29`（US 143441、GB 143444、JP 143462、TW 143470）。出現在建議清單、排越前面 ≈ 搜尋量越高。amp-api 沒用（要 token）。
2. **iTunes Search API**：`https://itunes.apple.com/search?term=<kw>&country=<cc>&entity=software&limit=50`。記錄結果數、前 10 名 userRatingCount 總和／最大值（大 = 競爭強或大 app 攔截）、競品排名。
3. 競品名稱推斷它們的關鍵字。

註：前 10 名評分總和常被和本題無關的大 app 拉高（例 reminder 有 Remind 學校 app），只當「競爭強度」看。

## US
| 關鍵字 | 建議清單 | 前10評分和 | 我們的機會 |
|---|---|---|---|
| last time tracker | 「last time」第1個建議 | 197k（真正同類最大 Last Time Tracker 636，$5.99） | **高需求、同類弱** |
| last time | 有 | 210k | 中高 |
| days since | 「days since」第1 | 1.48M（I Am Sober、DayCount） | 需求高、競爭強 |
| days since tracker | 第3 | 237k | 中 |
| when did i | 「when did」第1，且有 when did i last… 多個 | 92（極弱） | **需求中、競爭最弱** |
| how long ago | 不在「how long」前8（多是交往天數） | 1.68M | 低相關 |
| habit tracker | 第2 | 1.07M | 紅海，只放 keywords |
| chore(s) tracker | 「chore」第1 chores tracker | 952k | 中 |
| reminder(s) | 第1 reminders | 3.2M | 紅海 |
| last done | 無建議 | 19.5k | 低 |
When'd I（Aslla，$2.99）：「when did i」排第12，「last time tracker」前50沒有。

## GB
同 US 結構，量小一個數量級。last time tracker 前10評分和 16k（最大同類 53）；when did i 17；mot reminder 有需求但被 Vehicle Smart（102k）佔。When'd I（£2.99）在「when did i」排第10。「how long」建議中有 how long since / how long ago。

## JP
| 關鍵字 | 建議 | 前10評分和 | 備註 |
|---|---|---|---|
| いつやった | 「いつ」第1（いつやった？）| 22k | 現役王者 いつやった？(677評分)，同名 app 12個 → 紅海 |
| 最後はいつ | 「最後」第1 | 2.6k | 最後はいつ？(2,566、¥1,000) |
| 最後にやった日 | 無建議 | 128 | 已有「なんにちぶり？- 最後にやった日の記録」、Itsu(96) 用到 → **我們的日文名撞名** |
| 何日ぶり | 無建議（「何日」下是 何日経った/何日目） | 52 | 競爭極弱、需求低-中 |
| いつぶり | — | 118k（大 app 攔截）；同類 0 評分 | 可放 keywords |
| 家事／記録／習慣 | 皆第1 | 47k／294k／140k | 大詞，keywords 用 |
いつだったっけ（Aslla，¥500）：最後にやった日第6、いつやった第31。

## TW（工具支援）
| 關鍵字 | 建議 | 前10評分和 | 備註 |
|---|---|---|---|
| 上次 / 上次是什麼時候 | 「上次」前8個建議 **全是同類 app** | 16–17 | 需求有、所有同類評分都≤5 → **最好打** |
| 多久沒 | 「多久」無建議 | 19 | 低 |
| 好久沒 | 只有「好久不見了」 | 522 | 需求低 |
| 家事紀錄 | 「家事」第1 家事 | 1.5k | 中 |
| 提醒 | 第1 提醒事項 | 67k | 大詞 |
| 習慣 | — | 25k | 大詞 |
上次是什麼時候 - 家事·保養紀錄（Aslla，NT$90）：「上次是什麼時候」第1、「上次」第2、「家事紀錄」第3。

## 建議（提案，尚未改商店欄位）
| | Name | Subtitle | Keywords |
|---|---|---|---|
| US | Been Ages: Last Time Tracker（28 B，保留） | Days Since Chores & Reminders（29 B；原句的 last 和名稱重複） | when,did,ago,how,long,habit,routine,log,clean,task,home,upkeep,filter,done,counter,history,record（97 B） |
| GB | 保留（28 B） | 保留 Days since chores, MOT & more（29 B） | reminder,when,did,ago,how,long,habit,routine,oven,boiler,service,toothbrush,kettle,bedding,descale（98 B；拿掉 contacts,clean,radiator 換 when did / how long ago） |
| JP | Been Ages：何日ぶり？（15 字／27 B） | 最後にやった日がわかる記録（13 字／39 B） | いつやった,いつぶり,前回,日数,経過,家事,掃除,習慣,通知,カウント（36 字／90 B） |
| TW | Been Ages：好久沒做了（15 字／27 B） | 上次是什麼時候？天數紀錄（12 字／36 B） | 多久,幾天,家事,提醒,保養,打掃,習慣,間隔,週期,更換（29 字／69 B） |
三欄互不重複已用腳本檢查。Apple 名稱／副標題以 30「字元」計，keywords 100 字元；上面全部也在 100 bytes 內。

命名：
- US/GB：「last time tracker」需求最清楚、真正同類都很弱，保留在名稱。when did i 放 keywords 拿下 When'd I 的主詞。
- JP：「いつやった」「最後はいつ」已被數千評分 app 佔，「最後にやった日」已被他人用 → 改名用「何日ぶり」，原詞移副標題／keywords。
- TW：修正先前建議：「上次是什麼時候」是**唯一有建議清單需求**的詞，不該只放 keywords；名稱用好久沒做了做區隔，副標題放「上次是什麼時候」。
- 上架後若要真正 popularity 分數，再評估 Apple Ads。
