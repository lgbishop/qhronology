#!/usr/bin/env bash
bash ../renderers/static.sh -i "icon" -o "$(basename "$0" ".sh")" -d "$(pwd)/../output" -F "svg" -c true -H 64 -V 64 -q 100
