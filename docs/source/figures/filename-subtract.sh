#!/usr/bin/env bash
for file in *circuit_*; do
    mv "$file" "${file//circuit_/}"
done
