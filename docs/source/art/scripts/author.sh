#!/usr/bin/env bash
bash ../renderers/static.sh -i "author" -o "$(basename "$0" ".sh")-light" -d "$(pwd)/../output" -F "pdf,svg" -E "xelatex" -T "" -c true -H 2000 -q 100
