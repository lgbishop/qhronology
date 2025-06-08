#!/usr/bin/env bash
bash ../renderers/animate.sh -i "cover-back" -o "$(basename "$0" ".sh")" -d "$(pwd)/../output" -F "pdf" -e "clock" -c true -B true -t 8 -C 60 -S 40 -E 3.5 -T "0.45:26:52"
