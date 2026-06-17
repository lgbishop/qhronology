#!/usr/bin/env bash
PATH_INPUT="./"

for f in $(find "$PATH_INPUT" -type f -name "*.log"); do
    echo "Deleting $f"
    rm -f "$f"
done
