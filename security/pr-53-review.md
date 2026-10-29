# PR #53 複審（tinytoolshedhq/app，Been Ages IAP，head 2a1f957）
結論：**通過**（策略取捨可接受，不阻擋）

驗證：10 檔 +562/-58；跟 main 沒有衝突；jest 522/522 全過（TZ=UTC、Asia/Taipei）；secret 掃描無真實 secret；IAP 相關程式沒有 console 輸出，不印收據或交易資料。Checklist：沒動到 podspec、媒體套件、app.json（buildNumber 仍是 12）。5 個語系都有加 iap.processing。

## 取捨評估：購買事件未驗證時保留解鎖並標記待確認 — 可接受
- 偽造門檻高、買斷價值低，風險可接受。審核員重開 app 仍是解鎖狀態，符合 2.1(b)。
- 啟動時以 entitlements 為準；明確撤銷立即鎖回；其餘情況依策略處理（追蹤中）。

## 發現
- 已知低風險項，追蹤中；完整內容待修正合併後補上。
- L2｜去重 key 在缺少交易 id 時的退回行為：不會卡住或漏交易，可接受。
- L2｜Paywall / Settings 防連點鎖正確釋放。
- L2｜buildNumber 仍是 12，下次 EAS build 前必須改成 >12（ASC 最高 12）。
