#!/usr/bin/env bash
grep -v "file = {" references.bib > references-clean.bib && mv -f references-clean.bib references.bib
grep -v "urldate = {" references.bib > references-clean.bib && mv -f references-clean.bib references.bib
