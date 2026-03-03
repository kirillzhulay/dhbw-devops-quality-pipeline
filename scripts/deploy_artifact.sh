#!/usr/bin/env bash
set -euo pipefail

ARTIFACT_PATH="${1:-dist/pipeline-artifact.zip}"
TARGET_DIR="${2:-deploy/target}"

if [[ ! -f "$ARTIFACT_PATH" ]]; then
  echo "Artifact not found: $ARTIFACT_PATH" >&2
  exit 1
fi

mkdir -p "$TARGET_DIR"
cp "$ARTIFACT_PATH" "$TARGET_DIR/pipeline-artifact.zip"

echo "Deployed artifact to $TARGET_DIR/pipeline-artifact.zip"