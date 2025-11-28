#!/usr/bin/env bash

set -euo pipefail

# Change to the spec component directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPEC_DIR="$SCRIPT_DIR/../components/sysrev_client/spec"
cd "$SPEC_DIR"

echo "Generating OpenAPI client..."
uv run openapi-python-client generate \
    --path openapi.json \
    --config gen-config.yaml \
    --overwrite \
    --fail-on-warning

# Move generated files to components/sysrev_client/spec
mv temp-project/gen .
rm -rf temp-project

echo "Updating spec component exports..."
python "$SCRIPT_DIR/update_exports.py"

echo "Done! OpenAPI client generated and exports updated."