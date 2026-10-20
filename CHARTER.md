# Charter / standing rules
- Reply to Chun in Traditional Chinese (zh-TW). Ask Chun only about important things.
- Use Cursor models only.
- Business: free download + one-time purchase; zero operating cost (no server).
- Minimal, polished UI. App follows the phone's system language. Taiwan is a light test market.
- Previews before development. Walkthroughs as GIF (<3MB), not mp4.
- EAS free plan: 15 builds/month — validate locally first, batch changes. **Every EAS build needs Chun's approval.**
- **Every post, comment or reply needs Chun's approval.** No auto-commenting. No fake or multiple accounts.
- Credentials only via masked inputs, never in chat — and never in this repo.
- 碼農 opens PRs, never pushes to main. 漏洞大師 reviews every app PR and never edits code. Merge/EAS also wait for 阿姨's test-flows.md pass.

## 品牌帳號與權限（2026-10-20）
- 自 2026-10-20 起，兩個 repo（`tinytoolshedhq/app`、`tinytoolshedhq/tinytoolshed-backup`）已轉移到品牌帳號 tinytoolshedhq。所有 GitHub 操作只用 tinytoolshedhq，絕不使用 Chun 的個人帳號 ChunWang1998。
- 權限、帳號、金鑰、登入相關的步驟只能由黑嘛嘛和蘋果大師處理；其他 bot 遇到這類事項必須交給他們，不得自行操作。
- 免費方案的私人 repo 沒有分支保護，因此一律開 PR，不直接推 main。

## 社群內容規則（Chun，2026-10-20）
- 每週一（台北時間）各國學習一次最高流量貼文：分析開頭鉤子、語氣、結構、結尾互動方式，更新到 `marketing/social/phrase-bank/<國家>.md`。只學習、更新用語庫，不做大量回覆。
- 各國腳本由小編自己寫，不統一成同一套，要符合當地語氣和習慣。
- IG Reels 用 CapCut 免費版剪輯＋加字幕，不用付費 AI 生成工具。

## App PR 規則（Chun，2026-10-20）
- 每個 app PR（`tinytoolshedhq/app`）必須先通過漏洞大師的安全審查。
- 審查通過後，可憐的碼農負責通知胖嘟嘟阿姨。
- 阿姨必須實際跑一次 `bots/user-tester/test-flows.md` 裡的流程。
- 只有阿姨通過後，才能合併或打包（EAS）。
- 備份 repo 的純文件 PR 免跑使用者測試。
