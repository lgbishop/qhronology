#!/usr/bin/env bash
rm -rf ./_build/doctest
sphinx-build -M doctest ./source ./_build --fresh-env --define root_doc="index" --define exclude_patterns="index_latex.rst"
