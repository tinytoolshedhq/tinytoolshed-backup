# PR #33（ad48908，base d3a510c → main）de/fr 多語系 — 結論：通過（2 項低，非阻擋）

註：box 上的 /workspace/security（包含舊報告與 repo clone）在本次審查前已不存在，已重新 clone。先前的報告 pr-*-review.md 已遺失，本報告是重新建立的。

## 1. 端側語音閘門（de/fr）
- JS speech.js 的 LANG 新增 de→de-DE、fr→fr-FR；Swift mappedLocale 新增 hasPrefix("de")→de-DE、hasPrefix("fr")→fr-FR。i18n 的 resolveTag 也加了 de/de-*、fr/fr-*。
- 實際呼叫端 AiVoiceView 一律傳 getLocale()，而 getLocale() 只可能是 en/zh-Hant/ja/de/fr（未知語系 fallback 為 en）。這五個值在檢查（Swift）與 start（JS）兩邊對到同一個 BCP-47 標籤。
- 實測（臨時 jest）：de→檢查 'de'、start de-DE；fr→fr-FR；de-CH→de-DE；fr-CA→fr-FR；undefined→en/en-US。startSpeech 在 mod.start 前的同步閘門仍在，requiresOnDeviceRecognition 仍固定為 true。
- **L1（低，縱深防禦）**：startSpeech({locale}) 若收到未解析的原始語系（例如 'es'），檢查會以 Swift 的 fallback `return tag` 檢查 'es'，但 start 用的是 speechLocale('es')=en-US，兩邊不一致。目前沒有呼叫端會傳原始語系，所以無法被利用。
  - 位置：app3/mobile/src/lib/ai/speech.js 的 supportsOnDeviceSpeech/startSpeech；AppleFoundationModelsModule.swift:108。
  - 修正：在 startSpeech 先算出 `const lang = speechLocale(locale)`，並把同一個 lang 傳給 supportsOnDeviceSpeech 和 start。Swift 未知語系改為回傳 en-US 或直接回傳 false（fail-closed）。

## 2. 字型來源與授權
- 三個 TTF 的 table 組成與 base 相同。name table ID 0/1/2/3/4/5/6/13/14 與 base 完全相同：family 為 BeenAgesRounded；copyright 註明 "Reserved Font Name NaikaiFont"；license URL 為 OFL。fontRevision、unitsPerEm、vendor 都沒變。
- cmap 只新增 48 個字元（«»ÀÂÄÆÇÈÉÊËÎÏÔÖ×ÙÛÜßàâäæçèéêëîïôöùûüÿŒœŸ‘’‚“”„‹›），沒有刪除任何字元；原有 869 個 glyph 的 outline 完全相同。
- 來源比對：從 README 與 scripts/subset-naikai.sh 指定的上游 github.com/max32002/naikaifont（tw/NaikaiFont-{Regular,SemiBold,Bold}.ttf）下載原檔，逐一比對全部 917 個 cmap glyph 的 outline 與 advance width：Regular、SemiBold、Bold 都是 0 差異。結論：沒有外來的 glyph 或 binary。
- 大小：每個檔案增加 9–15 KB，對 48 個 glyph 來說合理。
- OFL.txt 和 README.txt 都在，而且沒有修改。修改版沒有使用 Reserved Font Name 作為 family 名稱，符合 OFL 1.1。
- 覆蓋率：check-font-coverage.js/.py 都已加入 languages/de.json、fr.json 和 ios/de.json、ios/fr.json，三個 keyword JSON 也在其中；font-coverage.test 有斷言。兩支腳本實際執行都顯示 OK。

## 3. 權限與隱私文字
- de/fr 的 InfoPlist（prebuild 後有 de、de-DE、fr、fr-FR 四個 lproj）中，麥克風與語音辨識說明都表達「只在本機、不送到網路」，與強制端側的實作一致。CFBundleLocalizations 已加上 de、fr。
- **L2（低，文案）**：de 的 NSPhotoLibraryAddUsageDescription 把「分享卡片」譯成「Anteilskarte」，這是誤譯（Anteil 是股份、份額的意思），建議改為「Teilkarte」或「Karte zum Teilen」。另外 de 語音說明中的「Einträge zu merken」語意偏「記住」，建議改為「hinzuzufügen」。不涉及安全。
- gh-pages 的 privacy/support 頁沒有 de/fr 版本；此 PR 沒有改動 gh-pages，現有的英文段落已經涵蓋。選配：之後可以補上。

## 4. AI de/fr 解析與免費上限
- 本 PR 只改了 phrases.json、categoryKeywords、iconKeywords、reminderKeywords 這些資料；repository.js、AiChatScreen、apply/ruleParser/relative、components 都沒有變。寫入路徑仍是佇列內的 addActivity 和 logActivityNow，10 個項目、10 筆紀錄、同日去重都在資料層執行。
- 288 個 regex 都能編譯，用 5000 字元的惡意輸入測試，每個都在 50ms 以內，沒有 ReDoS。
- 實測：「vor 3 Tagen, alle 2 Wochen」→ 3 天前、提醒 14 天；log 意圖不帶日期；「dans 5 jours」不會產生未來日期。「il y a 500000 jours」會算出年份 657，但 createActivity 的 isoYearInRange（2000–2100）會丟掉這筆，結果是沒有紀錄，無害。這個行為在既有語系也一樣，不是新問題。

## 5. 其他
- package.json、lockfile、eas.json、audit-ci.json、plugins、iap.js、entitlements.js、reminderSchedule.js 都沒有修改。沒有新依賴；prebuild 的 entitlements 是空 dict，沒有 UIBackgroundModes。
- 與 main（4c6e6bb，#32 buildNumber 9）的 merge-tree 沒有衝突，合併後 buildNumber 為 9（PR 分支本身是 8）。

## 檢查
- gitleaks（d3a510c..pr33，2 個 commit）沒有洩漏。
- audit-ci 通過，白名單仍只有 GHSA-vfj7-8cjw-p6xm 和 GHSA-86w9-cpqp-85rv。
- jest 28 組、347 個測試，預設時區和 America/New_York 都通過。
- expo-doctor 18/18；prebuild ios 成功。
