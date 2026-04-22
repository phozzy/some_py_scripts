{
  description = "Develop Python on Nix with uv";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs =
    { nixpkgs, ... }:
    let
      inherit (nixpkgs) lib;
      forAllSystems = lib.genAttrs lib.systems.flakeExposed;
    in
    {
      devShells = forAllSystems (
        system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
          pythonGrammar = pkgs.vimPlugins.nvim-treesitter.grammarToPlugin
            pkgs.vimPlugins.nvim-treesitter.builtGrammars.python;
        in
        {
          default = pkgs.mkShell {
            packages = with pkgs; [
              python3
              uv
              cocogitto
              pyright
              ruff
            ];

            # env = lib.optionalAttrs pkgs.stdenv.isLinux {
            #   # Python libraries often load native shared objects using dlopen(3).
            #   # Setting LD_LIBRARY_PATH makes the dynamic library loader aware of libraries without using RPATH for lookup.
            #   LD_LIBRARY_PATH = lib.makeLibraryPath pkgs.pythonManylinuxPackages.manylinux1;
            # };

            shellHook = ''
              unset PYTHONPATH
              uv sync
              . .venv/bin/activate
              export NVIM_FORMATTERS='{"python": ["ruff_format"]}'
              export NVIM_LINTERS='{"python": ["ruff"]}'
              export NVIM_TREESITTER_PARSER_PATH="${pythonGrammar}"
            '';
          };
        }
      );
    };
}
