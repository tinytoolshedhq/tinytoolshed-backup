# PR #30 規則解析測試

- commit：origin/main `f737573`（含 PR #30 `d3a510c`）
- 對象：`src/lib/ai/ruleParser.js` 的 `parseRules`（網頁版與無 Apple Intelligence 時使用的離線規則解析）
- 基準時間：2026-10-20 16:00（週二），以 Jest 執行，沒有改 repo

共 38 句，判定錯誤或有問題 18 句（標 ✗）。

| 語言 | 句子 | 類型 | 名稱 | 提醒(天) | 上次(天前) | 判定 |
|---|---|---|---|---|---|---|
| zh-Hant | 每兩週換濾心，上次是昨天 | create | 換濾心 | 14 | 1 | ✓ |
| zh-Hant | 每週倒垃圾 | create | 倒垃圾 | 7 | 0 | ✓ |
| zh-Hant | 每3個月換牙刷，上次是上個月 | create | 換牙刷 | 90 | 30 | ✓ |
| zh-Hant | 每天吃維他命 | create | 吃維他命 | 1 | 0 | ✓ |
| zh-Hant | 提醒我每月繳房租 | create | 提醒我 繳房租 | 30 | 0 | ✗ 名稱含「提醒我」 |
| zh-Hant | 上週六洗床單，以後每兩週一次 | create | 六洗床單 以後 一次 | 14 | 7 | ✗ 名稱「六洗床單 以後 一次」；上次算成 7 天前（應為 3 天前 10/17） |
| zh-Hant | 我多久沒換床單了？ | query_since | 換床單 |  |  | ✓ |
| zh-Hant | 上次洗車是什麼時候 | query_since | 洗車 |  |  | ✓ |
| zh-Hant | 這週要做什麼？ | query_week |  |  |  | ✓ |
| zh-Hant | 今天有什麼要做 | create | 有什麼要做 |  | 0 | ✗ 應為查詢今天，被當成新增「有什麼要做」 |
| zh-Hant | 剛剛洗了車 | log | 洗 車 |  |  | ✗ 類型正確，名稱「洗 車」多空格（實機模糊比對有對到洗車） |
| zh-Hant | 我剛換了貓砂 | create | 我剛換 貓砂 | 7 | 0 | ✗ 應為記錄，被當成新增「我剛換 貓砂」 |
| zh-Hant | 昨天澆了花 | create | 澆 花 |  | 1 | ✗ 應為記錄（昨天），被當成新增「澆 花」 |
| zh-Hant | 洗好碗了 | create | 洗好碗 |  | 0 | ✗ 應為記錄，被當成新增 |
| zh-Hant | 記一下剪頭髮 | create | 剪頭髮 | 42 | 0 | ✓ |
| zh-Hant | 三天前換了床單 | create | 三天前換 床單 | 14 | 0 | ✗ 應為記錄 3 天前，被當成新增「三天前換 床單」且上次＝今天 |
| zh-Hant | 每隔10天澆花 | create | 每隔10天澆花 | 3 | 0 | ✗ 提醒變每 3 天（應 10 天），名稱含「每隔10天」 |
| en | change the filter every 2 weeks, last done yesterday | create | change the filter | 14 | 1 | ✓ |
| en | take out the trash weekly | create | take out the trash | 7 | 0 | ✓ |
| en | water the plants every 3 days | create | water the plants | 3 | 0 | ✓ |
| en | how long since I washed the sheets? | query_since | washed the sheets |  |  | ✗ 類型正確，名稱為過去式 "washed the sheets"，可能比對不到 |
| en | when did I last wash the car | query_since | wash the car |  |  | ✓ |
| en | what is due this week? | query_week |  |  |  | ✓ |
| en | what do I need to do today | create | what do I need to do |  | 0 | ✗ 應為查詢，被當成新增 |
| en | just washed the car | log | washed the car |  |  | ✓ |
| en | I changed the litter | create | I changed the litter |  | 0 | ✗ 應為記錄，被當成新增 |
| en | watered the plants yesterday | create | watered the plants |  | 1 | ✗ 應為記錄（昨天），被當成新增 |
| en | add haircut every 6 weeks | create | haircut | 42 | 0 | ✓ |
| en | remind me to pay rent monthly | create | pay rent | 30 | 0 | ✓ |
| ja | 2週間ごとにフィルター交換、前回は昨日 | create | にフィルター交換 | 14 | 1 | ✗ 名稱多「に」 |
| ja | 毎週ゴミ出し | create | ゴミ出し | 7 | 0 | ✓ |
| ja | 毎日ビタミンを飲む | create | ビタミンを飲む | 1 | 0 | ✓ |
| ja | シーツを最後に洗ったのはいつ？ | create | シーツを最後に洗ったのはいつ | 14 | 0 | ✗ 應為查詢，被當成新增 |
| ja | 今週は何をする？ | query_week |  |  |  | ✓ |
| ja | さっき洗車した | log | 洗車 |  |  | ✓ |
| ja | 猫砂を替えた | create | 猫砂を替えた | 7 | 0 | ✗ 應為記錄，被當成新增 |
| ja | 昨日水やりした | log | 昨日水やり |  |  | ✗ 類型為記錄，但名稱「昨日水やり」且未算成昨天 |
| ja | 3か月ごとに歯ブラシ交換 | create | に歯ブラシ交換 | 90 | 0 | ✗ 名稱多「に」 |
