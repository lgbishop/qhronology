#!/usr/bin/env bash
rm -rf ./_build/latex
rm -rf ./source_latex

cp -r ./source ./source_latex
REMOVAL='.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames'
find ./source_latex -type f -exec perl -0777 -i.bak -pe "s/\Q$REMOVAL\E//g" {} +
find ./source_latex -type f -name "*.bak" -exec rm {} +

sphinx-build -M latex ./source_latex ./_build --tag "latex" --write-all --fresh-env --define root_doc="index_latex" --define exclude_patterns="index.rst"
cp -r ./source/figures/output/* ./_build/latex/
cp -r ./source/art/output/* ./_build/latex/
cp -r ./source/fonts/ ./_build/latex/

perl -i -pe 's/\\subsubsection\*{Examples}/\\subparagraph\*{\\hspace{-0.58cm}Examples}/g' "./_build/latex/qhronology.tex"

perl -i -pe 's/sphinxVerbatim/Verbatim/g' "./_build/latex/qhronology.tex"
perl -i -pe 's/\[commandchars=\\\\\\\{\\\}\]/\[breaklines, breakanywhere, breaknonspaceingroup, breaksymbolleft=\\tiny\\textcolor{color_defaults}{\\ensuremath{\\hookrightarrow}}, breaksymbolright=\\tiny\\textcolor{color_defaults}{\\ensuremath{\\hookleftarrow}}, breakafter=\\,\/\\space, breakaftersymbolpre=, breaksymbolindentrightnchars=3, breaksymbolseprightnchars=1, breakpreferspaces=true, commandchars=\\\\\\\{\\\}\]/g' "./_build/latex/qhronology.tex"

perl -i -pe 's/\\begin{quote}/\\begin{adjustwidth}{0em}{1em}\\begin{quote}/g' "./_build/latex/qhronology.tex"
perl -i -pe 's/\\end{quote}/\\end{quote}\\end{adjustwidth}/g' "./_build/latex/qhronology.tex"

perl -i -pe 's/\\begin{sphinxadmonition}{note}{Note:}/\\vspace{-0.25\\baselineskip}\\begin{sphinxadmonition}{note}{Note:}/g' "./_build/latex/qhronology.tex"
perl -i -pe 's/\\end{sphinxadmonition}/\\end{sphinxadmonition}\\vspace{-0.5\\baselineskip}/g' "./_build/latex/qhronology.tex"

# perl -i -pe 's/\\sphinxhref{https:\/\/doi.org/\\sphinxhreftt{https:\/\/doi.org/g' "./_build/latex/qhronology.tex"
# perl -i -pe 's/\\sphinxhref{https:\/\/arxiv.org/\\sphinxhreftt{https:\/\/arxiv.org/g' "./_build/latex/qhronology.tex"

perl -i -pe 's/\\sphinxhref{https:\/\/qhronology.org}{Qhronology}/\\sphinxhrefnott{https:\/\/qhronology.org}{Qhronology}/g' "./_build/latex/qhronology.tex"
perl -i -pe 's/\\sphinxhref{https:\/\/www.python.org}{Python}/\\sphinxhrefnott{https:\/\/www.python.org}{Python}/g' "./_build/latex/qhronology.tex"
perl -i -pe 's/\\sphinxhref{https:\/\/sympy.org}{SymPy}/\\sphinxhrefnott{https:\/\/sympy.org}{SymPy}/g' "./_build/latex/qhronology.tex"
perl -i -pe 's/\\sphinxhref{https:\/\/numpy.org}{NumPy}/\\sphinxhrefnott{https:\/\/numpy.org}{NumPy}/g' "./_build/latex/qhronology.tex"
perl -i -pe 's/\\sphinxhref{https:\/\/pypi.org\/project\/qhronology}{PyPI}/\\sphinxhrefnott{https:\/\/pypi.org\/project\/qhronology}{PyPI}/g' "./_build/latex/qhronology.tex"
perl -i -pe 's/\\sphinxhref{https:\/\/pip.pypa.io}{pip}/\\sphinxhrefnott{https:\/\/pip.pypa.io}{pip}/g' "./_build/latex/qhronology.tex"
perl -i -pe 's/\\sphinxhref{https:\/\/www.sphinx-doc.org}{Sphinx}/\\sphinxhrefnott{https:\/\/www.sphinx-doc.org}{Sphinx}/g' "./_build/latex/qhronology.tex"
perl -i -pe 's/\\sphinxhref{https:\/\/github.com\/sphinx-doc\/sphinx}{repository}/\\sphinxhrefnott{https:\/\/github.com\/sphinx-doc\/sphinx}{repository}/g' "./_build/latex/qhronology.tex"
perl -i -pe 's/\\sphinxhref{https:\/\/github.com\/mathjax\/MathJax}{MathJax}/\\sphinxhrefnott{https:\/\/github.com\/mathjax\/MathJax}{MathJax}/g' "./_build/latex/qhronology.tex"
perl -i -pe 's/\\sphinxhref{https:\/\/github.com\/mrdoob\/three.js}{three.js}/\\sphinxhrefnott{https:\/\/github.com\/mrdoob\/three.js}{three.js}/g' "./_build/latex/qhronology.tex"
perl -i -pe 's/\\sphinxhref{https:\/\/github.com\/pyodide\/pyodide}{Pyodide}/\\sphinxhrefnott{https:\/\/github.com\/pyodide\/pyodide}{Pyodide}/g' "./_build/latex/qhronology.tex"
perl -i -pe 's/\\sphinxhref{https:\/\/github.com\/sympy\/sympy}{SymPy}/\\sphinxhrefnott{https:\/\/github.com\/sympy\/sympy}{SymPy}/g' "./_build/latex/qhronology.tex"
perl -i -pe 's/\\sphinxhref{https:\/\/github.com\/numpy\/numpy}{NumPy}/\\sphinxhrefnott{https:\/\/github.com\/numpy\/numpy}{NumPy}/g' "./_build/latex/qhronology.tex"
perl -i -pe 's/\\sphinxhref{https:\/\/docs.sympy.org\/latest\/tutorials\/intro-tutorial\/simplification.html}{SymPy documentation: Simplification}/\\sphinxhrefnott{https:\/\/docs.sympy.org\/latest\/tutorials\/intro-tutorial\/simplification.html}{SymPy documentation: Simplification}/g' "./_build/latex/qhronology.tex"
perl -i -pe 's/\\sphinxhref{https:\/\/docs.sympy.org\/latest\/modules\/simplify\/simplify.html}{SymPy documentation: Simplify}/\\sphinxhrefnott{https:\/\/docs.sympy.org\/latest\/modules\/simplify\/simplify.html}{SymPy documentation: Simplify}/g' "./_build/latex/qhronology.tex"

perl -i -pe 's/TypeAliasForwardRef\\DUrole{p}{\(}\\DUrole{s}{\\textquotesingle{}mat\\textquotesingle{}}\\DUrole{p}{\)}/mat/g' "./_build/latex/qhronology.tex" # https://github.com/sphinx-doc/sphinx/issues/14003

perl -i -pe 's/\\sphinxtableatstartofbodyhook\\sphinxstyletheadfamily/\\sphinxtableatstartofbodyhook\\sphinxstyletheadfamily\\rmfamily/g' "./_build/latex/qhronology.tex"
perl -i -pe 's/\\sphinxhline\\sphinxstyletheadfamily/\\sphinxhline\\sphinxstyletheadfamily\\rmfamily/g' "./_build/latex/qhronology.tex"

# perl -i -pe 's/\\S\{\}/\\S\{\}\\itshape/g' "./_build/latex/qhronology.tex"

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
exiftool -overwrite_original -Title="Qhronology: Documentation, Examples, and Theory" -Author="Lachlan G. Bishop" -Subject="" -Creator="" -Producer="" ./_build/latex/Qhronology_documentation.pdf
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
