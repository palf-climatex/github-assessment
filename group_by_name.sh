#!/bin/sh

if [ $# -ne 1 ]; then
  echo "Usage: $0 <path-to-json-file>"
  exit 1
fi

jq 'to_entries
    | map(.key as $repo | .value[] | {type, name, repo: $repo})
    | group_by(.type + ": " + .name)
    | map({(.[0].type + ": " + .[0].name): map(.repo)})
    | add' "$1"
