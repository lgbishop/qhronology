let
  # Pin to a specific nixpkgs commit for reproducibility
  # Simply change the hash in the URL to switch versions
  pkgs = import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/d65262787557f7b520ea29ce828e5e0e42a48dec.tar.gz") {};
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
      # sphinxcontrib-katex # MathJax (v3) is better for now
    ]))
    # other non-python packages here
  ];
}
