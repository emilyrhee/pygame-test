{ pkgs ? import <nixpkgs> { } }:

let
  pythonEnv = pkgs.python3.withPackages(ps: with ps; [
    pygame
  ]);
in pkgs.mkShell {
  name = "momo-pygame";
  packages = [
    pythonEnv
  ];
}
