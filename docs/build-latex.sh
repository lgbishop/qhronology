#!/usr/bin/env bash
rm -rf ./_build/latex

cp -r ./source ./source_latex
REMOVAL='.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames'
find ./source_latex -type f -exec perl -0777 -i.bak -pe "s/\Q$REMOVAL\E//g" {} +
find ./source_latex -type f -name "*.bak" -exec rm {} +

sphinx-build -M latex ./source_latex ./_build --tag "latex" --write-all --fresh-env --define root_doc="index_latex" --define exclude_patterns="index.rst"
make --directory=./_build/latex

PAGES=$(pdfinfo qhronology.pdf | awk '/^Pages:/ {print $2}')

echo "\documentclass[a4paper]{article}
\pagestyle{empty}
\begin{document}
\null
\newpage
\end{document}" > ./_build/latex/blank.tex

pdflatex -output-directory="./_build/latex/" ./_build/latex/blank.tex

# pdfjam --outfile "./_build/latex/Qhronology_documentation.pdf" -- ./source/art/output/cover-front.pdf ./source/art/output/cover-inner-left.pdf ./source/art/output/cover-inner-right.pdf ./_build/latex/blank.pdf ./_build/latex/qhronology.pdf #./source/art/output/cover-inner-left.pdf ./source/art/output/cover-inner-right.pdf ./source/art/output/cover-back.pdf
pdftk ./source/art/output/cover-front.pdf ./source/art/output/cover-inner-left.pdf ./source/art/output/cover-inner-right.pdf ./_build/latex/blank.pdf ./_build/latex/qhronology.pdf cat output ./_build/latex/first.pdf

if [[ $((PAGES % 2)) != 0 ]]; then
    # pdfjam --outfile "./_build/latex/Qhronology_documentation.pdf" -- ./_build/latex/Qhronology_documentation.pdf ./_build/latex/blank.pdf
    pdftk ./_build/latex/first.pdf ./_build/latex/blank.pdf cat output ./_build/latex/second.pdf
    mv -f ./_build/latex/second.pdf ./_build/latex/first.pdf
fi
# pdfjam --outfile "./_build/latex/Qhronology_documentation.pdf" --pdftitle "Qhronology - Documentation, Examples, and Theory" --pdfauthor "Lachlan G. Bishop" --pdfsubject "" --pdfkeywords "" -- ./_build/latex/Qhronology_documentation.pdf ./source/art/output/cover-inner-left.pdf ./source/art/output/cover-inner-right.pdf ./source/art/output/cover-back.pdf
pdftk ./_build/latex/first.pdf ./source/art/output/cover-inner-left.pdf ./source/art/output/cover-inner-right.pdf ./source/art/output/cover-back.pdf cat output ./_build/latex/Qhronology_documentation.pdf

exiftool -overwrite_original -all:all= ./_build/latex/Qhronology_documentation.pdf
exiftool -overwrite_original -Title="Qhronology - Documentation, Examples, and Theory" -Author="Lachlan G. Bishop" -Subject="" -Creator="" -Producer="" ./_build/latex/Qhronology_documentation.pdf
exiftool -overwrite_original -xmp:all= ./_build/latex/Qhronology_documentation.pdf

# pdftk ./_build/latex/Qhronology_documentation.pdf update_info info.txt output ./_build/latex/Qhronology.pdf

rm ./_build/latex/blank.*
rm ./_build/latex/qhronology.pdf
mv -f ./_build/latex/Qhronology_documentation.pdf ./_build/latex/Qhronology.pdf

rm -rf ./source_latex
mv -f ./_build/latex/Qhronology.pdf ./_build/Qhronology.pdf
rm -rf ./_build/latex
mkdir ./_build/latex
mv -f ./_build/Qhronology.pdf ./_build/latex/
