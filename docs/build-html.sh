#!/usr/bin/env bash
rm -rf ./_build/html

cp -r ./source ./source_html
REMOVAL='.. only:: latex

   .. toctree::
      :maxdepth: 2
      :caption: Architecture
      :class: hidden

      architecture.rst'
find ./source_html -type f -exec perl -0777 -i.bak -pe "s/\Q$REMOVAL\E//g" {} +
find ./source_html -type f -name "*.bak" -exec rm {} +

sphinx-build -M html ./source_html ./_build --tag "html" --write-all --fresh-env --define root_doc="index" --define exclude_patterns="index_latex.rst"
touch ./_build/html/.nojekyll
rm -rf ./source_html
