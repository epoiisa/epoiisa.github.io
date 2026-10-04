#!/bin/bash
set -euo pipefail

site_dir="$(cd -- "$(dirname -- "$0")" && pwd)"
cd -- "$site_dir"

export BUNDLE_PATH="$site_dir/.preview/gems"
export BUNDLE_GEMFILE="$site_dir/_preview/Gemfile"
if ! bundle check >/dev/null 2>&1; then
  bundle install
fi

printf 'Local preview: http://127.0.0.1:8765/\n'
printf 'Pages and styles refresh automatically. Press Control-C to stop.\n'

exec bundle exec jekyll serve \
  --host 127.0.0.1 \
  --port 8765 \
  --livereload \
  --livereload-port 35729 \
  --destination "$site_dir/.preview/site"
