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
          RStudio = pkgs.rstudioWrapper.override { packages = with pkgs.rPackages; [ heatmaply partykit caret pROC rattle rpart_plot RColorBrewer ]; };
        in
        with pkgs;
        {
          devShells.default = mkShell rec {
            buildInputs = [
              RStudio
              (pkgs.python3.withPackages (python-pkgs: with python-pkgs; [
                pyarrow
                pandas
                matplotlib
                seaborn
                scipy
                scikitlearn
                graphviz
                mlxtend
                nltk
                gensim
              ]))
            ];
          };
        }
      );
}
