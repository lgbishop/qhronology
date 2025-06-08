with import <nixpkgs> {};
with pkgs.python3Packages;

let
  docs-python-packages = python-packages: with python-packages; [
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
    # sphinxcontrib-katex # MathJax (v3) is currently better

    # For doctest
    sympy
    numpy
  ];
  python-sphinx = python.withPackages docs-python-packages;
in
mkShell {
  buildInputs = [
    python-sphinx # python environment defined above
    pdftk # Command-line tool for working with PDFs
    exiftool # Tool to read, write and edit EXIF meta information
  ];

  shellHook = ''
    # bash build-latex.sh
    # bash build-html.sh
  '';

}
