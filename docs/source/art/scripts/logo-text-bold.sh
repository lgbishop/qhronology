#!/usr/bin/env bash
bash ../renderers/static.sh -i "logo-text-bold-light" -o "$(basename "$0" ".sh")-light" -d "$(pwd)/../output" -F "pdf,svg" -E "xelatex" -T "" -c true -H 2000 -q 100
bash ../renderers/static.sh -i "logo-text-bold-dark" -o "$(basename "$0" ".sh")-dark" -d "$(pwd)/../output" -F "pdf,svg" -E "xelatex" -T "" -c true -H 2000 -q 100
