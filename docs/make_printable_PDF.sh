#!/usr/bin/env bash
# Use this script to generate a print-ready textbook-like PDF document from the Qhronology.pdf file.

# The desired size of all pages in the document.
# SIZE='{210mm,297mm}' # A4
# SIZE='{176mm,250mm}' # B5
# SIZE='{210mm,280mm}' # 4:3 (A4 scale)
# SIZE='{210mm,262.5mm}' # 5:4 (A4 scale)
# SIZE='{189mm,252mm}' # 4:3 A4 at 90% scale
# SIZE='{178.5mm,238mm}' # 4:3 A4 at 85% scale
# SIZE='{192mm,256mm}' # 4:3
SIZE='{192mm,240mm}' # 5:4
# SIZE='{196mm,245mm}' # 5:4

# Trim of the upper edge (in millimetres).
# For best results, set this to the difference between input paper's (should be A4) height and the height of desired aspect ratio (at equivalent scale).
# (May also need slight adjustment due to how LaTeX renders the source PDF.)
TRIM=34.5

# Alternating margin padding in centimetres
MARGIN=0.60

# Scaling factors for the interior pages and the covers.
# Decrease this to give larger margins on every edge (e.g., increased page bleed).
SCALE_PAGES=1.10
SCALE_COVER=1.08

# The background to be used to extend the cover pages (if necessary).
COLOUR="002569"
PAGES=$(pdfinfo ./_build/latex/Qhronology.pdf | awk '/^Pages:/ {print $2}')

rm -rf ./_build/latex/printable
mkdir ./_build/latex/printable
rm ./_build/latex/Qhronology_printable.pdf

# Front cover
pdfjam --papersize $SIZE \
 --scale $SCALE_COVER \
 --pagecommand {\\thispagestyle{empty}\\definecolor{maincolor}{HTML}{$COLOUR}\\pagecolor{maincolor}} \
 --outfile ./_build/latex/printable/Qhronology_printable-cover_front.pdf --no-keepinfo \
 ./_build/latex/Qhronology.pdf 1

# Back cover
pdfjam --papersize $SIZE \
 --scale $SCALE_COVER \
 --pagecommand {\\thispagestyle{empty}\\definecolor{maincolor}{HTML}{$COLOUR}\\pagecolor{maincolor}} \
 --outfile ./_build/latex/printable/Qhronology_printable-cover_back.pdf --no-keepinfo \
 ./_build/latex/Qhronology.pdf $PAGES

# Front inside covers
pdfjam --trim "0cm 0cm 0cm ${TRIM}mm" --clip true \
 --papersize $SIZE \
 --outfile ./_build/latex/printable/Qhronology_printable-inside_front.pdf --no-keepinfo \
 ./_build/latex/Qhronology.pdf 2,3

# Back inside covers
pdfjam --trim "0cm 0cm 0cm ${TRIM}mm" --clip true \
 --papersize $SIZE \
 --outfile ./_build/latex/printable/Qhronology_printable-inside_back.pdf --no-keepinfo \
 ./_build/latex/Qhronology.pdf $(($PAGES - 2)),$(($PAGES - 1))

# All other pages
pdfjam --papersize $SIZE \
 --scale $SCALE_PAGES \
 --outfile ./_build/latex/printable/Qhronology_printable-pages.pdf --no-keepinfo \
 ./_build/latex/Qhronology.pdf 4-$(($PAGES - 3))

PAGES_INNER=$(pdfinfo ./_build/latex/printable/Qhronology_printable-pages.pdf | awk '/^Pages:/ {print $2}')

for PAGE in $(seq 1 $((PAGES_INNER))); do

    PADDING=$(printf '0%.0s' $(seq 1 ${#PAGES_INNER}))
    PADDED="${PADDING}${PAGE}"
    PAGE_PADDED="${PADDED: -${#PAGES_INNER}}"

    echo $PAGE
    echo $PAGE_PADDED
    if [[ $((PAGE % 2)) != 0 ]]; then
        echo "ODD" # Add margin on the right

        pdfjam --papersize $SIZE \
         --offset "-${MARGIN}cm -2.25mm" \
         --outfile "./_build/latex/printable/Qhronology_printable-pages_$PAGE_PADDED.pdf" --no-keepinfo \
         ./_build/latex/printable/Qhronology_printable-pages.pdf $((PAGE))

    else
        echo "EVEN" # Add margin on the left

        pdfjam --papersize $SIZE \
          --offset "${MARGIN}cm -2.25mm" \
         --outfile "./_build/latex/printable/Qhronology_printable-pages_$PAGE_PADDED.pdf" --no-keepinfo \
         ./_build/latex/printable/Qhronology_printable-pages.pdf $((PAGE))

    fi
done

pdftk ./_build/latex/printable/Qhronology_printable-pages_*.pdf \
 cat output ./_build/latex/printable/Qhronology_printable-pages.pdf

# Combine
pdftk ./_build/latex/printable/Qhronology_printable-cover_front.pdf \
 ./_build/latex/printable/Qhronology_printable-inside_front.pdf \
 ./_build/latex/printable/Qhronology_printable-pages.pdf \
 ./_build/latex/printable/Qhronology_printable-inside_back.pdf \
 ./_build/latex/printable/Qhronology_printable-cover_back.pdf \
 cat output ./_build/latex/Qhronology_printable.pdf

# Clean
rm -rf ./_build/latex/printable
exiftool -overwrite_original -all:all= ./_build/latex/Qhronology_printable.pdf
exiftool -overwrite_original -Title="Qhronology: Documentation, Examples, and Theory" -Author="Lachlan G. Bishop" -Subject="" -Creator="" -Producer="" ./_build/latex/Qhronology_printable.pdf
exiftool -overwrite_original -xmp:all= ./_build/latex/Qhronology_printable.pdf
