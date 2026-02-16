let
  # Pin to a specific nixpkgs commit for reproducibility
  # Simply change the hash in the URL to switch versions
  pkgs = import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/2343bbb58f99267223bc2aac4fc9ea301a155a16.tar.gz") {};
in pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (python-pkgs: with python-pkgs; [
      pillow
      sphinx
      pydata-sphinx-theme
      # sphinx-sitemap
      sphinx-design
      sphinx-togglebutton
      sphinx-copybutton
      sphinxcontrib-bibtex
      pybtex
      myst-parser
      sphinx-autoapi
      # sphinxcontrib-katex # MathJax (v3) is better for now

      # For doctest
      sympy
      numpy
    ]))
    pkgs.pdftk # Command-line tool for working with PDFs
    pkgs.exiftool # Tool to read, write and edit EXIF meta information
  ];

  shellHook = ''
    unset SOURCE_DATE_EPOCH
    # bash build-latex.sh
    # bash build-html.sh
  '';
}
