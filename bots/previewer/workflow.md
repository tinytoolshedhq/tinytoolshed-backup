# previewer 工作流程

## 規則
- 用繁體中文回報。
- 只用 Cursor 自己的模型。
- 不改正式 repo，也不 commit 或 push；要看程式碼時用唯讀的 checkout，或用 git archive 匯出到 /tmp。
- 不 build（EAS 每月只有 15 次，而且要 Chun 核准）。
- 黑嘛嘛說「先不要直接傳給 Chun」時，只回報給黑嘛嘛。
- 小事自己決定並記下來，只問 Chun 重要的事。

## 設計預覽
1. 先讀 main 現在的樣式（字型、顏色、圖示、吉祥物），再照 ui-principles 和 no-ai-look 的原則做。
2. 做一份 HTML 原型（393×852）：
   - 用 `?theme=light|dark` 切換主題。
   - 用 `?s=<preset>` 直接打開某個畫面。
   - 用 `?bare=1` 隱藏控制按鈕。
3. 用 Playwright 截圖：DPR 2，淺色和深色各一組，再拼成一張 overview.png（上排淺色、下排深色）。
4. 錄影設定：Playwright 393×852、DPR 2、觸控模式、zh-TW、畫出觸控點。
   - 用 ffmpeg 加速成 1.5 倍，輸出 H.264 yuv420p、faststart 的 mp4。
   - GIF 一定要另外出一份（Chun 打不開 mp4），盡量壓在 3MB 以下：寬 360、10–12fps、96–128 色。
5. 每張畫面都要逐張看過，再回報：路徑、需要 Chun 決定的事，以及自己先決定的小地方。

## 實機驗證錄影
1. 用 git archive 匯出指定的 commit 到 /tmp，執行 `npm ci`，再用 `npx expo start --web` 開網頁版。
2. 用 Playwright 從空的 storage 開始錄，需要時直接寫入示範資料。
3. 截圖放在 bugs-real/，一個驗證項目一張，console 另外存成檔案。
4. 錄完停掉 Expo，確認 8081 沒有回應。
5. 回報每一項通過或失敗、bug 的重現步驟，以及推測的原因。

## 注意
- 共用電腦可能會被重置，重要的東西要備份到這個 repo。影片和大檔不要放進來。
