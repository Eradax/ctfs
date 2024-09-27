{ pkgs ? import <nixpkgs> {} }:

with pkgs;

mkShell {
  packages = [(haskellPackages.ghcWithPackages (pkgs: with pkgs; [extra cabal-install transformers MonadRandom tardis]))];
}
