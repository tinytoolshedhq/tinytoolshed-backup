# Been Ages｜fr-FR App Store 商店頁

> **機器草稿（沒有母語校對）｜DRAFT, needs Chun approval**。不能直接上架，需母語者校對＋Chun 核准。

- 撰寫：2026-10-20（台北時間）｜歐洲小編。依據：en-GB 修訂版（`been-ages-gb-outreach.md`）、美國版（`been-ages-us-outreach.md` §4）、`../learning/by-country/FR.md`、app 1.1.1 現有功能（`/workspace/bv/app3/mobile`）。
- Chun 規則：法國只做 ASO＋短影音，不在 X／Threads 發文。
- 主打：「Achat unique, sans abonnement」＋資料留在 iPhone。不提 widget、iCloud、備份。
- 檢查：`python3 ../scripts/check-aso.py fr`（結果附在最後）。

## 欄位
| 欄位 | 內容 | 字元 | bytes | 上限 |
|---|---|---|---|---|
| Name | Been Ages : la dernière fois | 28 | 29 | 30 字元 |
| Subtitle | Rappels : ménage, entretien… | 28 | 31 | 30 字元 |
| Keywords | contrôle,technique,ramonage,chaudière,brosse,dents,lentilles,tâches,maison,routine,suivi,jours | 94 | 97 | 100 bytes |
| Promotional text | Quand avez-vous changé votre brosse à dents ou fait ramoner la cheminée pour la dernière fois ? Un geste, et Been Ages compte les jours. Achat unique, sans abonnement. | 167 | 171 | 170 字元 |

## Description（1856 字元／4000）
> Been Ages se souvient à votre place des choses que vous ne faites que de temps en temps.
>
> Draps changés ? Bouilloire détartrée ? Nouvelle tête de brosse à dents ? Un geste, et Been Ages enregistre la date. Plus tard, vous voyez exactement depuis combien de temps : 1 mois et 17 jours, et non « environ un mois ».
>
> CE QUE VOUS AVEZ
> • Noté en un seul geste. Aucun formulaire.
> • Le temps exact écoulé, en mois et en jours. Sans arrondi.
> • Un rappel quand c'est le moment : chaque semaine, toutes les 2 semaines, chaque mois, chaque année ou à l'intervalle de votre choix. Rappel manqué ? L'app vous le redit 3 jours plus tard.
> • Les éléments en retard se repèrent tout de suite.
> • Historique, notes et statistiques simples pour chaque élément : combien de fois, en moyenne, et le plus long écart.
> • Ajout de la prochaine échéance à votre Calendrier.
> • Une carte à partager quand c'est enfin fait.
> • Mode clair ou sombre.
> • Supprimé par erreur ? Annulez, ou retrouvez-le pendant 30 jours dans « Supprimés récemment ».
>
> DES IDÉES POUR COMMENCER
> Contrôle technique, ramonage, entretien de la chaudière, rendez-vous chez le dentiste, lentilles, brosse à dents, draps, détartrage de la bouilloire, dégivrage du congélateur, nettoyage du four, vermifuge du chat, ou tout simplement la dernière fois que vous avez appelé votre grand-mère.
>
> VOS DONNÉES RESTENT CHEZ VOUS
> Sans compte, sans inscription. Vos données restent sur votre iPhone et nous ne voyons pas ce que vous notez.
>
> ACHAT UNIQUE, SANS ABONNEMENT
> Téléchargement gratuit, jusqu'à 10 éléments et 10 enregistrements par élément. Un achat unique vous donne des éléments illimités et d'autres styles de cartes. Sans abonnement. Déjà acheté ? Vous pouvez restaurer votre achat à tout moment.
>
> Créé par un développeur indépendant chez Tiny Toolshed. Vos retours sont les bienvenus.

## 截圖文案（前 3 張講好處）
| # | 建議畫面 | 文案 | 字元 | 備註 |
|---|---|---|---|---|
| 1 | 清單頁（多個項目＋天數） | Voyez d'un coup d'œil depuis quand | 34 | 好處 |
| 2 | 單一項目詳情（幾個月幾天） | En mois et en jours, sans arrondi | 33 | 好處 |
| 3 | 提醒設定 | Un rappel quand c'est le moment | 31 | 好處 |
| 4 | 新增／編輯 | Noté en un seul geste | 21 |  |
| 5 | 設定頁「資料」或隱私說明 | Sans compte. Vos données restent sur l'iPhone. | 46 |  |
| 6 | 買斷頁 | Achat unique, sans abonnement | 29 |  |
| 7 | 深色模式 | Clair ou sombre, à vous de choisir | 34 |  |

## 在地例子查證
| 例子 | 查證 | 來源 |
|---|---|---|
| Contrôle technique | 小客車 4 年內首檢，之後每 2 年；逾期罰 135 € | https://www.service-public.gouv.fr/particuliers/vosdroits/F2878 |
| Ramonage | 法定至少每年 1 次，多數省份每年 2 次；罰 450 € | https://www.service-public.gouv.fr/particuliers/vosdroits/F32437 |
| Entretien de la chaudière | 【推論】法國燃氣／燃油鍋爐有年度保養義務，未在本輪查證 | — |

## 備註
- 稱呼用 **vous**（法國商店頁常見【推論】）。
- 法文標點：冒號、問號前有空格（這裡用一般空格；上架時可換成不換行窄空格，字數不變）。
- Keywords 把「contrôle technique」拆成 `contrôle,technique` 兩個字，Apple 會自動組合【推論】；`brosse,dents` 同理。
- Name 備選：`Been Ages : depuis quand ?`（26）。
- 說明文的功能都對過 app 1.1.1：一鍵記錄、幾個月幾天、提醒（週／2 週／月／年／自訂間隔，錯過 3 天後再提醒）、逾期、歷史＋備註＋統計（次數、平均、最長間隔）、加到行事曆、分享卡、深色模式、最近刪除 30 天、免費 10 個項目（每項 10 筆紀錄）（Chun 定案；app 1.1.1 程式碼目前是 10 項＋每項 10 筆，需碼農改）、買斷後無限制＋更多卡片樣式、恢復購買。
- ⚠️ **app 介面目前沒有德文／法文**（只有 en、zh-Hant、ja）。商店頁是法國文、打開卻是英文，可能招來負評【推論】。

## 待 Chun 決定
1. 要不要等 app 有法國文介面再上法國文商店頁。
2. 找誰做母語校對。
3. ~~定價~~ 已定案：€2.99 一次買斷，無上市優惠，不開家人共享，不用「freischalten／débloquer」（Chun 2026-10-20 定案：等同 US $2.99 的價格點；MetaRun 2026-10-12 由 App Store Connect API 取得的對照表：GB £2.99、DE €2.99、FR €2.99，上架前請在 ASC 再確認）。
4. 截圖要用法國文介面重拍（目前沒有法國文介面）。

## 檢查結果
```
== fr
  name            28 chars    29 bytes  limit 30 chars  OK
  subtitle        28 chars    31 bytes  limit 30 chars  OK
  keywords        94 chars    97 bytes  limit 100 bytes  OK
  promo          167 chars   171 bytes  limit 170 chars  OK
  description   1856 chars  1935 bytes  limit 4000 chars  OK
  caption 1     34 chars  Voyez d'un coup d'œil depuis quand
  caption 2     33 chars  En mois et en jours, sans arrondi
  caption 3     31 chars  Un rappel quand c'est le moment
  caption 4     21 chars  Noté en un seul geste
  caption 5     46 chars  Sans compte. Vos données restent sur l'iPhone.
  caption 6     29 chars  Achat unique, sans abonnement
  caption 7     34 chars  Clair ou sombre, à vous de choisir
  name∩subtitle      none
  name∩keywords      none
  subtitle∩keywords  none
  keyword repeats    none
  spaces in keywords: False
  plural overlaps: none
  banned words: none
  RESULT: PASS
```
