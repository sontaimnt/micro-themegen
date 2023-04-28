{
  description = "A devbox shell";

  inputs = {
    nixpkgs.url = "https://github.com/nixos/nixpkgs/archive/f80ac848e3d6f0c12c52758c0f25c10c97ca3b62.tar.gz";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { 
    self,
    nixpkgs,
    flake-utils 
  }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = (import nixpkgs {
          inherit system;
          config.allowUnfree = true;
        });
      in
      {
        devShell = pkgs.mkShell {
          buildInputs = with pkgs; [
            python311Packages.pip
          ];
        };
      }
    );
}
