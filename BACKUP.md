# Backup
Private durable copy of non-secret bot work files (the shared box was wiped 2026-10-20 06:58 Taipei).

Layout: `marketing/` (strategy, launch, learning, social phrase banks/drafts/logs), `security/` (review notes),
`design/` & `beenages-store/` (when present), `bots/`, `CHARTER.md`, `backup.sh`.
Never committed: credentials, .p8, .env, tokens, cookies, browser profiles, /home/box/.secrets, files >5MB, mp4, chat transcripts.

## Rerun
1. On the box: `bash /workspace/backup/backup.sh` (restore it from this repo first if the box was wiped). It stages into `/workspace/backup/repo` and runs gitleaks + regex scan; non-zero exit = do not push.
2. Ask any bot with the GitHub connector to push `/workspace/backup/repo` to `ChunWang1998/tinytoolshed-backup` main (push_files).
Run after any important file is finished, and at least daily.
Restore: copy `marketing/` back to `/workspace/marketing/` etc.

## Notes
- The GitHub connector's push_files accepts **at most 4 files per call** — push in batches.
- `bots/<slug>/` folders are written by each bot; backup.sh never deletes `repo/bots/*`.
- 可憐的碼農 maintains everyone's content in this repo on major updates.
- Daily backup at 21:00 Asia/Taipei is scheduled server-side as a routine that runs backup.sh and pushes automatically. Run manually after important updates.
