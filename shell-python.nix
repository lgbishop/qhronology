let
  pkgs-system = import <nixpkgs> {};
  # pkgs-pinned = import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/205fd4226592cc83fd4c0885a3e4c9c400efabb5.tar.gz") {};
in pkgs-system.mkShell {
  packages = [
    (pkgs-system.python3.withPackages (python-pkgs: with python-pkgs; [
      sympy
      numpy
      ipython
    ]))
    pkgs-system.vscodium
  ];
}
