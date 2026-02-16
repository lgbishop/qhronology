#!/usr/bin/env bash
bash ../renderers/animate.sh -i "cover-front" -o "$(basename "$0" ".sh")" -d "$(pwd)/../output" -F "pdf" -l "$(pwd)/../output/logo-text-bold-dark.pdf" -c true -B false -t 8 -C 60 -S 40 -E 3.5 -T "2.9:53:7" #-e "clock

SIZE='{210mm,297mm}' # A4
SCALE=0.925
COLOUR="002569"

pdfjam --papersize $SIZE \
 --scale $SCALE \
 --pagecommand {\\thispagestyle{empty}\\definecolor{maincolor}{HTML}{$COLOUR}\\pagecolor{maincolor}} \
 --outfile ../output/cover-front.pdf --no-keepinfo \
 ../output/cover-front.pdf
