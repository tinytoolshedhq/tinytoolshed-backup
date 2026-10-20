#!/usr/bin/env bash
# Tiny Toolshed backup: sync allowed non-secret paths into ./repo, then secret-scan.
# After SCAN CLEAN: open a cloud agent on tinytoolshedhq/tinytoolshed-backup to create a PR;
# review, then merge. Do not use GitHub connector push_files or push main directly.
# Exit code != 0 means scan failed -> DO NOT open a PR.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"; OUT="$HERE/repo"
GL="$(command -v gitleaks || echo /home/box/bin/gitleaks)"
[ -x "$GL" ] || { mkdir -p /home/box/bin; curl -sL https://github.com/gitleaks/gitleaks/releases/download/v8.21.2/gitleaks_8.21.2_linux_x64.tar.gz | tar xz -C /home/box/bin gitleaks; GL=/home/box/bin/gitleaks; }
mkdir -p "$OUT"; find "$OUT" -mindepth 1 -maxdepth 1 ! -name bots -exec rm -rf {} +  # keep bots/* written by other bots
# copy SRC DST [glob-allowlist...] : skips secrets, >5MB, media, transcripts
copy() { python3 - "$@" <<'PY'
import sys,os,shutil,fnmatch
src,dst,*allow=sys.argv[1:]
bad=['.env*','*.p8','*.pem','*.key','*.p12','*.mobileprovision','*cookie*','*token*','*secret*','*.mp4','*.mov','*transcript*','*.zip','*.ipa']
for r,ds,fs in os.walk(src):
    ds[:]=[d for d in ds if d not in('node_modules','.git','.secrets')]
    for f in fs:
        p=os.path.join(r,f); l=f.lower()
        if any(fnmatch.fnmatch(l,b) for b in bad) or os.path.getsize(p)>5*2**20: continue
        if allow and not any(fnmatch.fnmatch(l,a) for a in allow): continue
        o=os.path.join(dst,os.path.relpath(p,src)); os.makedirs(os.path.dirname(o),exist_ok=True); shutil.copy2(p,o)
PY
}
# Allowed sources (add new ones here)
copy /workspace/marketing "$OUT/marketing"
[ -d /workspace/beenages-store ] && copy /workspace/beenages-store "$OUT/beenages-store"
[ -d /workspace/design ] && copy /workspace/design "$OUT/design" '*.html' '*.css' '*.md' '*.png' '*.gif' '*.svg'
mkdir -p "$OUT/security"; cp /workspace/security/*.md "$OUT/security/" 2>/dev/null || true
cp "$HERE"/{CHARTER.md,BACKUP.md,backup.sh,.gitignore} "$OUT/"; mkdir -p "$OUT/bots"; cp -rn "$HERE/bots/." "$OUT/bots/"; cp "$HERE/bots/README.md" "$OUT/bots/README.md"; cp "$HERE/README.md" "$OUT/" 2>/dev/null || true
# Secret scan (gitleaks + regex fallback). Prints file names only, never values.
"$GL" detect --no-git --source "$OUT" --redact --no-banner -r /tmp/gl-report.json >/dev/null 2>&1 || { echo "GITLEAKS FOUND ISSUES in:"; python3 -c "import json;[print(' ',f['File']) for f in json.load(open('/tmp/gl-report.json'))]"; exit 1; }
if rg -l -e 'BEGIN [A-Z ]*PRIVATE KEY' -e 'ghp_[A-Za-z0-9]{30,}' -e 'github_pat_' -e 'sk-[A-Za-z0-9]{20,}' -e 'AKIA[0-9A-Z]{16}' -e 'xox[baprs]-' "$OUT" --glob '!backup.sh'; then echo "REGEX SCAN HIT (files above)"; exit 1; fi
echo "SCAN CLEAN. $(find "$OUT" -type f | wc -l) files staged in $OUT"
