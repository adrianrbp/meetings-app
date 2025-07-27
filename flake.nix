{
  # Description of this flake project
  description = "Dev environment for Django meeting-planner app with Node.js and Python";

  inputs = {
    # Import nixpkgs (Nix packages) from a specific channel/version
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-23.05";

    # Import flake-utils for easier multi-platform support
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    # Create output for each supported system (x86_64-linux, etc)
    flake-utils.lib.eachDefaultSystem (system:
      let
        # Import pkgs for the given system (like the package set)
        pkgs = import nixpkgs {
          inherit system;
        };
      in {
        # Define a development shell environment named `devShell`
        devShell = pkgs.mkShell {
          # List packages/tools to be available in the shell
          buildInputs = with pkgs; [
            nodejs-18_x       # Node.js version 18.x
            python38         # Python 3.8 interpreter
            python38Packages.pip  # pip package manager for Python 3.8
            yarn              # Optional: Yarn package manager for Node.js
            git               # Git VCS tool
          ];

          # A small shell hook that runs when you enter the nix shell
          shellHook = ''
            echo "Welcome to your Django + Node.js dev environment!"
          '';
        };
      }
    );
}
