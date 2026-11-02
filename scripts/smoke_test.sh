#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
.venv/bin/python scripts/build_example.py --out exports/demo
.venv/bin/python -m pytest -q tests
echo "CAD smoke test passed; exports/demo contains the generated files."
