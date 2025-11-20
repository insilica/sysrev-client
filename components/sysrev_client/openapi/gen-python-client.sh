#!/usr/bin/env bash

set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"

uv run openapi-python-client generate \
    --path openapi.json \
    --config gen-config.yaml \
    --overwrite \
    --fail-on-warning
    
# Move generated files to components/sysrev_client/openapi
mv temp-project/gen .
rm -rf temp-project