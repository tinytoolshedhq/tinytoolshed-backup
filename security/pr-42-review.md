# PR #42 安全/隱私審查（tinytoolshedhq/app，head 365eae9）

結論：**通過**

## 範圍
14 檔 +512/-32：提醒時刻（所有頻率）、舊資料遷移 09:00、HH:MM 驗證與時分 clamp、第一列顯示、45 天顯示修正。

## 檢查結果
- gitleaks（diff）：無。gitleaks（全樹）：2 筆 generic-api-key 位於 app2/fetchData/*.py（846e…、6F30…），main 上已存在，非本 PR 引入。
- 新增行 regex（key/token/email/電話/EXPO_PUBLIC_/fetch/http/console/__proto__）：無命中。
- 依賴：package.json / lockfile 未改；@react-native-community/datetimepicker 9.1.0 原本即存在。無新網路呼叫。
- 通知：僅改排程時刻計算，仍為本機通知；privacy.html 不需更動。
- 寫入：未動 repository.js，寫入佇列、同日去重、10 項 / 10 筆限制不變；未來時間 clamp 不受影響。
- 遷移：loadState → migrateActivity → reminderConfigFromActivity → sanitizeReminderTime，缺值補 09:00、無法解析回落 09:00、不改 enabled。
- 驗證：zod activitySchema 改用 REMINDER_TIME_RE（嚴格 HH:MM）；parseHm/formatHm clamp 處理 NaN/負值/超界。
- npm ci、jest 502/502（預設 TZ 與 America/New_York）、audit-ci 通過、expo-doctor 18/18、expo prebuild ios 成功、merge-tree 對 main 無衝突。

## 發現
- L1（低/資訊）src/lib/reminderSchedule.js `importedReminderTime`、以及 activitySchema：目前 app 內沒有匯入路徑呼叫它們（只有測試使用），「匯入拒絕不合法 HH:MM」實際上尚未接到任何程式路徑。不構成風險；未來加匯入功能時務必使用 activitySchema.safeParse + importedReminderTime。
- L2（低/資訊）DetailScreen.js 仍硬寫 `'09:00'`，可改用 DEFAULT_REMINDER_TIME。純一致性。
