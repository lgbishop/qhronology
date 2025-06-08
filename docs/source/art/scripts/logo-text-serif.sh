#!/usr/bin/env bash
bash ../renderers/static.sh -i "logo-text-serif" -o "$(basename "$0" ".sh")" -d "$(pwd)/../output" -F "pdf,svg" -c true -H 2000 -q 100
