# Been Ages｜de-DE App Store 商店頁

> **機器草稿（沒有母語校對）｜DRAFT, needs Chun approval**。不能直接上架，需母語者校對＋Chun 核准。

- 撰寫：2026-10-20（台北時間）｜歐洲小編。依據：en-GB 修訂版（`been-ages-gb-outreach.md`）、美國版（`been-ages-us-outreach.md` §4）、`../learning/by-country/DE.md`、app 1.1.1 現有功能（`/workspace/bv/app3/mobile`）。
- Chun 規則：德國只做 ASO＋短影音，不在 X／Threads 發文。
- 主打：「Einmalkauf, kein Abo」＋資料留在裝置上（Daten bleiben lokal／auf deinem iPhone）。不提 widget、iCloud、備份。
- 檢查：`python3 ../scripts/check-aso.py de`（結果附在最後）。

## 欄位
| 欄位 | 內容 | 字元 | bytes | 上限 |
|---|---|---|---|---|
| Name | Been Ages: Zuletzt gemacht? | 27 | 27 | 30 字元 |
| Subtitle | Tage seit TÜV, Wartung & Co. | 28 | 29 | 30 字元 |
| Keywords | erinnerung,haushalt,putzplan,heizung,zahnbürste,kontaktlinsen,routine,termin,intervall,kalender,abo | 99 | 100 | 100 bytes |
| Promotional text | Wann hast du zuletzt die Zahnbürste gewechselt oder die Heizung warten lassen? Einmal tippen, Been Ages zählt die Tage. Einmalkauf, kein Abo, Daten bleiben lokal. | 162 | 164 | 170 字元 |

## Description（1844 字元／4000）
> Been Ages merkt sich die Dinge, die du nur ab und zu erledigst, damit du es nicht musst.
>
> Bettwäsche gewechselt? Wasserkocher entkalkt? Neuen Bürstenkopf eingesetzt? Einmal tippen, und Been Ages speichert das Datum. Später siehst du genau, wie lange es her ist: 1 Monat und 17 Tage statt „ungefähr ein Monat“.
>
> DAS BEKOMMST DU
> • Mit einem Tipp eingetragen. Keine Formulare.
> • Die genaue Zeit seit dem letzten Mal, in Monaten und Tagen. Nichts wird gerundet.
> • Eine Erinnerung, wenn es wieder fällig ist: wöchentlich, alle 2 Wochen, monatlich, jährlich oder in jedem Intervall, das du willst. Verpasst? Dann erinnert dich die App 3 Tage später noch einmal.
> • Überfällige Einträge fallen sofort auf.
> • Verlauf, Notizen und einfache Statistik für jeden Eintrag: wie oft, im Schnitt und die längste Pause.
> • Den nächsten Termin in deinen Kalender eintragen.
> • Eine Karte teilen, wenn du es endlich erledigt hast.
> • Heller oder dunkler Modus.
> • Aus Versehen gelöscht? Rückgängig machen oder 30 Tage lang unter „Zuletzt gelöscht“ wiederfinden.
>
> IDEEN FÜR DEN ANFANG
> TÜV (Hauptuntersuchung), Heizungswartung, Reifenwechsel, Zahnarzt-Kontrolle, Kontaktlinsen, Zahnbürste, Bettwäsche, Wasserkocher entkalken, Kühlschrank abtauen, Backofen putzen, Rauchmelder testen, Entwurmung für die Katze oder einfach: wann du zuletzt Oma angerufen hast.
>
> DEINE DATEN BLEIBEN BEI DIR
> Kein Konto, keine Anmeldung. Deine Daten bleiben auf deinem iPhone, und wir sehen nicht, was du einträgst.
>
> EINMALKAUF, KEIN ABO
> Kostenlos laden, mit bis zu 3 Einträgen. Mit einem Einmalkauf bekommst du unbegrenzt viele Einträge und weitere Kartenstile. Kein Abo. Schon gekauft? Du kannst deinen Kauf jederzeit wiederherstellen. [PENDING CHUN: 3 vs 10 items]
>
> Gemacht von einem einzelnen Entwickler bei Tiny Toolshed. Feedback ist jederzeit willkommen.

## 截圖文案（前 3 張講好處）
| # | 建議畫面 | 文案 | 字元 | 備註 |
|---|---|---|---|---|
| 1 | 清單頁（多個項目＋天數） | Sieh sofort, wie lange es her ist | 33 | 好處 |
| 2 | 單一項目詳情（幾個月幾天） | Genau in Monaten und Tagen, nie gerundet | 40 | 好處 |
| 3 | 提醒設定 | Erinnert dich, wenn es wieder fällig ist | 40 | 好處 |
| 4 | 新增／編輯 | Mit einem Tipp erledigt | 23 |  |
| 5 | 設定頁「資料」或隱私說明 | Kein Konto. Deine Daten bleiben auf dem iPhone. | 47 |  |
| 6 | 買斷頁 | Einmalkauf, kein Abo | 20 |  |
| 7 | 深色模式 | Hell oder dunkel, wie du willst | 31 |  |

## 在地例子查證
| 例子 | 查證 | 來源 |
|---|---|---|
| TÜV／HU | 小客車首次 36 個月、之後每 24 個月，法定 | https://www.dekra.de/de/faq-hauptuntersuchung/ |
| Heizungswartung | GEG §60 要求定期維護；BDH 建議每年一次（法律沒規定頻率） | https://www.enercity.de/magazin/mein-leben/heizungswartung |
| Reifenwechsel | 【推論】德國常見「O bis O」（Oktober bis Ostern）換冬胎習慣，未在本輪查證 | — |
| Rauchmelder testen | 【推論】一般建議每年檢查一次（DIN 14676），未在本輪查證 | — |

## 備註
- 稱呼用 **du**（德國生活類 app 常見【推論】）；要改成 Sie 需全篇改寫。
- 「TÜV」是口語，正式名稱是 Hauptuntersuchung（HU），說明文兩者並列。
- Keywords 有 `abo`：可能吃到「Abo」搜尋，但也會帶來找訂閱管理 app 的人【推論】；可改成 `kalender` 以外的字。
- Name 用問句「Zuletzt gemacht?」（最後一次做是什麼時候）；備選：`Been Ages: Wann zuletzt?`（24）。
- 說明文的功能都對過 app 1.1.1：一鍵記錄、幾個月幾天、提醒（週／2 週／月／年／自訂間隔，錯過 3 天後再提醒）、逾期、歷史＋備註＋統計（次數、平均、最長間隔）、加到行事曆、分享卡、深色模式、最近刪除 30 天、免費 3 個項目（Chun 定案；app 1.1.1 程式碼目前是 10 項＋每項 10 筆，需碼農改）、買斷後無限制＋更多卡片樣式、恢復購買。 [PENDING CHUN: 3 vs 10 items]
- ⚠️ **app 介面目前沒有德文／法文**（只有 en、zh-Hant、ja）。商店頁是德國文、打開卻是英文，可能招來負評【推論】。

## 待 Chun 決定
1. 要不要等 app 有德國文介面再上德國文商店頁。
2. 找誰做母語校對。
3. ~~定價~~ 已定案：€2.99 一次買斷，無上市優惠，不開家人共享，不用「freischalten／débloquer」（Chun 2026-10-20 定案：等同 US $2.99 的價格點；MetaRun 2026-10-12 由 App Store Connect API 取得的對照表：GB £2.99、DE €2.99、FR €2.99，上架前請在 ASC 再確認）。
4. 截圖要用德國文介面重拍（目前沒有德國文介面）。

## 檢查結果
```
== de
  name            27 chars    27 bytes  limit 30 chars  OK
  subtitle        28 chars    29 bytes  limit 30 chars  OK
  keywords        99 chars   100 bytes  limit 100 bytes  OK
  promo          162 chars   164 bytes  limit 170 chars  OK
  description   1844 chars  1898 bytes  limit 4000 chars  OK
  caption 1     33 chars  Sieh sofort, wie lange es her ist
  caption 2     40 chars  Genau in Monaten und Tagen, nie gerundet
  caption 3     40 chars  Erinnert dich, wenn es wieder fällig ist
  caption 4     23 chars  Mit einem Tipp erledigt
  caption 5     47 chars  Kein Konto. Deine Daten bleiben auf dem iPhone.
  caption 6     20 chars  Einmalkauf, kein Abo
  caption 7     31 chars  Hell oder dunkel, wie du willst
  name∩subtitle      none
  name∩keywords      none
  subtitle∩keywords  none
  keyword repeats    none
  spaces in keywords: False
  plural overlaps: none
  banned words: none
  RESULT: PASS
```
