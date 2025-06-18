#!/bin/sh

if [ $# -ne 1 ]; then
  echo "Usage: $0 <path-to-json-file>"
  exit 1
fi

awk '{
  print
  if ($0 ~ /^}/) exit
}' "$1" | jq '
  to_entries
  | map(select(.value | type == "array"))
  | map(.value[])
  | map(select(.type == "user" and has("name")))
  | map(.name)
  | unique
'
