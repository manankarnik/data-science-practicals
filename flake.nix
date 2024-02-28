{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem
      (system:
        let
          pkgs = import nixpkgs {
            inherit system;
          };
          RStudio = pkgs.rstudioWrapper.override { packages = with pkgs.rPackages; [ ggplot2 ]; };
        in
        with pkgs;
        {
          devShells.default = mkShell rec {
            buildInputs = [
              RStudio
              (pkgs.python3.withPackages (python-pkgs: [
                python-pkgs.pyarrow
                python-pkgs.pandas
                python-pkgs.matplotlib
                python-pkgs.seaborn
              ]))
            ];
          };
        }
      );
}
