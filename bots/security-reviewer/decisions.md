# 審查結論與已知風險

## 重點規則（審查時要確認）
- IAP：transactionVerified 只接受 `=== true`；有 revocationDate 就拒絕；連續 3 次驗證失敗才撤銷 Pro；正式版 allowSimulate=false。
- 免費版上限：10 個項目、每個項目 10 筆紀錄，在 repository.js 資料層檢查。所有寫入都走同一條 promise 佇列；Pro 失效後保留舊資料，只擋新增。
- 語音：只在裝置端辨識。啟動前先用 supportsOnDeviceSpeech(locale) 檢查，檢查和啟動用同一個語系，並且一律設 requiresOnDeviceRecognition: true；不支援的裝置就不啟動語音。
- AI：只用 SystemLanguageModel 裝置端模型，不用 Private Cloud Compute，也沒有網路呼叫；對話只放在記憶體。
- 字型：BeenAgesRounded（從 naikaifont 做的子集），必須保留 OFL.txt。

## 各 PR 結論
- #17：一開始驗證會在出錯時放行（fail-open），恢復購買和啟動檢查沒驗證就解鎖 Pro；修好後在 7507018 通過。
- #18、#19：天數計算錯誤修好後通過。
- #20：support.html 和 README 還寫 3 個項目；請碼農修好後直接合併，不用再審。
- #22：逾期判斷和小工具不一致；修好後在 bf1a86b 通過。
- #23、#24：分類上限 30、名稱重複檢查、icon 白名單；#24 字型少了 148 個字，在 #25 補齊。
- #25：遷移上限和逾期截斷問題修好後，在 49ab6b2 通過。
- #26：通過。
- #27：1.1.1 準備，通過。
- #28、#29：連點會造成同一天重複記錄、超過 10 筆上限，另外隱私權頁還寫著小工具；修好後在 3d119a2 和 32441af 通過。小工具和 App Group 已經清乾淨。
- #30、#31：語音可能改送 Apple 伺服器，和說明不一致；採方案 A（只用裝置端）修好，在 f9d0d71 和 73d478b 通過。
- #32：buildNumber 改成 9，通過。
- #33：德文和法文介面，通過；字型經比對和上游完全一致。
- #34：補上 NSPhotoLibraryUsageDescription，buildNumber 改成 10，通過。

## 已知風險（低）
- 從語音檢查完到建立辨識器之間有毫秒級空檔，如果剛好這時語言包被移除，套件在 ExpoSpeechRecognizer.swift:588 可能改用伺服器。可以用 patch-package 改成直接報錯。
- 語系對應建議統一成同一個 speechLocale()，Swift 遇到不認識的語系改回傳 false（#33 L1）。
- 新增項目和分類的寫入原本沒排進佇列，#30 已經一起排進去。

## 可以忽略
- lockfile 裡殘留的 expo-widgets 和 @expo/ui 條目，是 npm 記錄選用相依套件的正常寫法，不會被安裝。
- audit-ci 白名單裡的 braces 和 node-forge，是已評估過的既有例外。
- expo-doctor 在我這邊是 18/18、碼農那邊是 21/21，只是工具版本不同。
- 德文翻錯的「Anteilskarte」（股份卡）只是翻譯問題，不是安全問題。
- 「il y a 500000 jours」這類極端日期會被年份檢查丟掉，沒有影響。
