#!/bin/bash

help() {
   echo 'usage: install-postgis POSTGRES_MAJOR_VERSION POSTGIS_VERSION'
   echo '       install-postgis --help'
   echo
   exit 1
}

[ "$1" == "--help" ] || [ "$1" == "" ] || [ "$2" == "" ] && help


POSTGRES_MAJOR_VERSION="$1"
POSTGIS_VERSION="$2"

set -e # stop on error

apt-get install --no-install-recommends -y \
        postgresql-$POSTGRES_MAJOR_VERSION-postgis-$POSTGIS_VERSION \
        postgresql-$POSTGRES_MAJOR_VERSION-postgis-$POSTGIS_VERSION-scripts;
