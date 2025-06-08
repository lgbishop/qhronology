#!/usr/bin/env bash
rm -rf ./_build/html
sphinx-build -M html ./source ./_build --tag "html" --write-all --fresh-env --define root_doc="index" --define exclude_patterns="index_latex.rst"
touch ./_build/html/.nojekyll
