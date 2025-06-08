with import <nixpkgs> {};
with pkgs.python3Packages;

let
  packaging-python-packages = python-packages: with python-packages; [
    build
    setuptools
    twine
  ];
  python-packaging = python.withPackages packaging-python-packages;
in
mkShell {
  buildInputs = [
    python-packaging # python environment defined above
  ];

  shellHook = ''
    python3 -m build
    rm -rf ./qhronology-*
    rm -rf ./src/qhronology.egg-info
    # python3 -m twine upload dist/*
  '';

}
