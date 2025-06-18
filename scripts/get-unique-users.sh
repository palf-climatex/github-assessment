#!/bin/sh

if [ $# -ne 1 ]; then
  echo "Usage: $0 <path-to-json-file>"
  exit 1
fi

FILTER='
  to_entries
  | map(.value[] | select(.type == "user") | .name)
  | unique
'

jq "$FILTER" "$1"
