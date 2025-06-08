#!/usr/bin/env bash
PATH_INPUT="./text"
PATH_OUTPUT="./output"
THREADS=8
mkdir $PATH_OUTPUT

rm -f ./jobs-text.txt
for f in $PATH_INPUT/*.txt ; do
    echo "$f" >> ./jobs-text.txt
done

# For when you want to test only specific files:
# rm -f ./jobs-text.txt
# touch ./jobs-text.txt
# echo "./text/text_examples_algorithms_teleportation.txt" >> ./jobs-text.txt
# echo "./text/text_examples_docstrings_circuit_postselection.txt" >> ./jobs-text.txt
# echo "./text/text_examples_docstrings_circuit_cnotsqrtswap.txt" >> ./jobs-text.txt
# echo "./text/text_examples_docstrings_diagram_circuit_padding_horizontal_increase.txt" >> ./jobs-text.txt

mapfile -t jobs < ./jobs-text.txt

for FILE in "${jobs[@]}"; do
    (
    FILENAME="${FILE%.*}" # Remove extension
    FILENAME="${FILENAME##*/}" # Remove parent directories
    echo $FILE
    echo $FILENAME
    echo $PATH_INPUT

    xelatex -shell-escape -synctex=0 -interaction=batchmode -file-line-error -jobname="$FILENAME" -output-directory="$PATH_OUTPUT" \
    "\newcommand\Filename{\"$PATH_INPUT/$FILENAME.txt\"}" \
    "\input{render-text.tex}"
    # rm -f "$PATH_INPUT/wrapped-$FILENAME.txt"
    FILENAME="${FILENAME}"
    mv -f "$PATH_OUTPUT/$FILENAME.pdf" "$PATH_OUTPUT/$FILENAME-uncropped.pdf"
    pdfcrop --hires "$PATH_OUTPUT/$FILENAME-uncropped.pdf" "$PATH_OUTPUT/$FILENAME.pdf"
    pdf2svg "$PATH_OUTPUT/$FILENAME.pdf" "$PATH_OUTPUT/$FILENAME-light.svg"
    # magick "$FILENAME-light.svg" -channel RGB -negate "$FILENAME-dark.svg"
    magick -density 4000 "$PATH_OUTPUT/$FILENAME.pdf" -channel RGB -negate -threshold 10% -negate -transparent white -quality 100% -gravity center -background transparent "$PATH_OUTPUT/$FILENAME-light.png" # -extent 16000x
    magick "$PATH_OUTPUT/$FILENAME-light.png" -resize 10.0% -channel RGB -negate -threshold 10% -negate "$PATH_OUTPUT/$FILENAME-light.png" # -sharpen 0x1.0
    magick "$PATH_OUTPUT/$FILENAME-light.png" -channel RGB -negate "$PATH_OUTPUT/$FILENAME-dark.png"
    #magick "$PATH_OUTPUT/$FILENAME-light.png" -channel RGB -negate -background black -alpha remove -alpha off "$PATH_OUTPUT/$FILENAME-alphaless.png"

    # Remove white fill and strokes from the light-theme SVG.
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

rm -f ./jobs-text.txt
