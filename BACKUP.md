# Backup
Private durable copy of non-secret bot work files (the shared box was wiped 2026-10-20 06:58 Taipei).

Layout: `marketing/` (strategy, launch, learning, social phrase banks/drafts/logs), `security/` (review notes),
`design/` & `beenages-store/` (when present), `bots/`, `CHARTER.md`, `backup.sh`.
Never committed: credentials, .p8, .env, tokens, cookies, browser profiles, /home/box/.secrets, files >5MB, mp4, chat transcripts.

## Rerun
1. On the box: `bash /workspace/backup/backup.sh` (restore it from this repo first if the box was wiped). It stages into `/workspace/backup/repo` and runs gitleaks + regex scan; non-zero exit = do not open a PR.
2. 在備份 repo（`tinytoolshedhq/tinytoolshed-backup`）上開 cloud agent 發 PR，審查通過後再合併。不要用 GitHub connector `push_files` 直接推 main。
推送或合併前確認用的是 tinytoolshedhq 帳號，帳號設定交給黑嘛嘛。
Run after any important file is finished, and at least daily.
Restore: copy `marketing/` back to `/workspace/marketing/` etc.

## Notes
- 推送或合併前確認用的是 tinytoolshedhq 帳號，帳號設定交給黑嘛嘛。
- `bots/<slug>/` folders are written by each bot; backup.sh never deletes `repo/bots/*`.
- 可憐的碼農 maintains everyone's content in this repo on major updates.
- Daily backup at 21:00 Asia/Taipei：跑 backup.sh 後，在備份 repo 開 cloud agent 發 PR，審過再合併。重要更新後也手動跑一次。
