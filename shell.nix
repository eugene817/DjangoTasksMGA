{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "django-task-manager-env";

  buildInputs = [
    pkgs.python310

    pkgs.python310Packages.pip
    pkgs.python310Packages.virtualenv

    pkgs.python310Packages.django
    pkgs.python310Packages.djangorestframework

    pkgs.python310Packages.psycopg2

    pkgs.postgresql

    pkgs.docker
    pkgs.docker-compose
  ];

  shellHook = ''
    echo "Welcome to Django/DRF/PostgreSQL!"
  '';
}

