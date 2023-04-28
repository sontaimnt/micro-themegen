let
  pkgs = import
    (fetchTarball {
      url = "https://github.com/nixos/nixpkgs/archive/f80ac848e3d6f0c12c52758c0f25c10c97ca3b62.tar.gz";
    })
    { };
in
with pkgs;
mkShell {
  packages = [
      python311Packages.pip
  ];
}
