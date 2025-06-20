#!/usr/bin/env bash
PATH_INPUT="./latex"
PATH_OUTPUT="./output"
THREADS=8
mkdir $PATH_OUTPUT

rm -f ./jobs-latex.txt
for f in $(find "$PATH_INPUT" -type f -name "*.tex"); do
    echo "$f" >> ./jobs-latex.txt
done

# For when you want to test only specific files:
# rm -f ./jobs-latex.txt
# touch ./jobs-latex.txt
# echo "./latex/circuit_algorithm_adder_full_multiple_linear.tex" >> ./jobs-latex.txt
# echo "./latex/diagram_classes.tex" >> ./jobs-latex.txt
# echo "./latex/diagram_billiard-ball_paradox.tex" >> ./jobs-latex.txt
# echo "./latex/diagram_spacetime_minkowski.tex" >> ./jobs-latex.txt

mapfile -t jobs < ./jobs-latex.txt

for FILE in "${jobs[@]}"; do
    (

    DIR=$(dirname "$FILE") # Get the directory of the file

    FILENAME="${FILE%.*}" # Remove extension
    FILENAME="${FILENAME##*/}" # Remove parent directories

    PATH_RELATIVE="${dir#$PATH_INPUT/}" # Get the relative path from $PATH_INPUT

    pdflatex -shell-escape -synctex=0 -interaction=batchmode -file-line-error -jobname="$FILENAME" -output-directory="$PATH_OUTPUT" "$PATH_INPUT/$PATH_RELATIVE/$FILENAME.tex"
    mv -f "$PATH_OUTPUT/$FILENAME.pdf" "$PATH_OUTPUT/$FILENAME-uncropped.pdf"
    pdfcrop --hires "$PATH_OUTPUT/$FILENAME-uncropped.pdf" "$PATH_OUTPUT/$FILENAME.pdf"
    pdf2svg "$PATH_OUTPUT/$FILENAME.pdf" "$PATH_OUTPUT/$FILENAME-light.svg"
    # magick "$FILENAME-light.svg" -channel RGB -negate "$FILENAME-dark.svg"

    if [[ $FILE != *"circuit"* ]]; then
        magick -density 4000 "$PATH_OUTPUT/$FILENAME.pdf" -quality 100% -gravity center -background transparent "$PATH_OUTPUT/$FILENAME-light.png" # -extent 16000x
        magick "$PATH_OUTPUT/$FILENAME-light.png" -resize 10.0% "$PATH_OUTPUT/$FILENAME-light.png" # -sharpen 0x1.0
        magick "$PATH_OUTPUT/$FILENAME-light.png" -channel RGB -negate "$PATH_OUTPUT/$FILENAME-dark.png"
    else
        magick -density 4000 "$PATH_OUTPUT/$FILENAME.pdf" -channel RGB -negate -threshold 10% -negate -transparent white -quality 100% -gravity center -background transparent "$PATH_OUTPUT/$FILENAME-light.png" # -extent 16000x
        magick "$PATH_OUTPUT/$FILENAME-light.png" -resize 10.0% -channel RGB -negate -threshold 10% -negate "$PATH_OUTPUT/$FILENAME-light.png" # -sharpen 0x1.0
        magick "$PATH_OUTPUT/$FILENAME-light.png" -channel RGB -negate "$PATH_OUTPUT/$FILENAME-dark.png"
    fi
    # magick "$PATH_OUTPUT/$FILENAME-light.png" -channel RGB -negate -background black -alpha remove -alpha off "$PATH_OUTPUT/$FILENAME-alphaless.png"

    # Remove white fill and strokes from the light-theme SVG
    sed -i -e 's/fill="rgb(100%, 100%, 100%)" fill-opacity="1"/fill="rgb(100%, 100%, 100%)" fill-opacity="0"/g' "$PATH_OUTPUT/$FILENAME-light.svg"
    sed -i -e 's/stroke="rgb(100%, 100%, 100%)" stroke-opacity="1"/stroke="rgb(100%, 100%, 100%)" stroke-opacity="0"/g' "$PATH_OUTPUT/$FILENAME-light.svg"
    # Create the dark-theme SVG by copying the light-theme version and then invert the colours
    cp -f "$PATH_OUTPUT/$FILENAME-light.svg" "$PATH_OUTPUT/$FILENAME-dark.svg"
    perl -i -pe 's/rgb\((.*?)%, (.*?)%, (.*?)%\)/"rgb(" . (100 - $1) . "%, " . (100 - $2) . "%, " . (100 - $3) . "%)"/ge' "$PATH_OUTPUT/$FILENAME-dark.svg"

    rm -f "$PATH_OUTPUT/$FILENAME.aux"
    rm -f "$PATH_OUTPUT/$FILENAME.log"
    rm -f "$PATH_OUTPUT/$FILENAME-uncropped.pdf"
    # rm -f "$PATH_OUTPUT/$FILENAME.pdf"
    ) &

    if (( $(jobs -p | wc -w) == $THREADS )); then
        wait -n
    fi
done
wait

rm -f ./jobs-latex.txt
