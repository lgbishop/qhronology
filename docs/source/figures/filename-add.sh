#!/usr/bin/env bash
for file in *; do
    mv "$file" "circuit_$file"
done
