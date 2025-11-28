#!/usr/bin/env bash

set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"

echo "Generating OpenAPI client..."
uv run openapi-python-client generate \
    --path openapi.json \
    --config gen-config.yaml \
    --overwrite \
    --fail-on-warning

# Move generated files to components/sysrev_client/openapi
mv temp-project/gen .
rm -rf temp-project

echo "Updating openapi component exports..."
python update_exports.py

echo "Done! OpenAPI client generated and exports updated."