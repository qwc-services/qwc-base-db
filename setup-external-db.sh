#!/bin/bash

help() {
   echo 'usage: setup-external-db.sh'
   echo '       setup-external-db.sh --help'
   echo
   echo '   This script is meant to be used to set up an'
   echo '   external postgres instance to be used for QWC.'
   echo
   echo '   It will install Alembic and other stuff on the'
   echo '   machine where it's executed on, so it's suggested'
   echo '   to run it in a thorow away VM or inside a'
   echo '   container or pod.'
   echo
   echo '   The target postgres instance *needs* to have postgis'
   echo '   already installed. See install-postgis.sh for a'
   echo '   script that will do it.'
   echo
   echo '   It will add a qwc_demo DB.'
   echo
   echo '   You can set the below environment variables. If not'
   echo '   set then the following defaults will be used:'
   echo
   echo "   - QWC_CONFIG_DB_GIT_REPO=$QWC_CONFIG_DB_GIT_REPO_DEFAULT"
   echo "   - ALEMBIC_VERSION=$ALEMBIC_VERSION_DEFAULT"
   echo "   - POSTGRES_USER=$POSTGRES_USER_DEFAULT"
   exit 1
}

echo "this is currently untested! Uncomment this line if you want to proceed" && exit 1

# defaults:
#
QWC_CONFIG_DB_GIT_REPO_DEFAULT=https://github.com/qwc-services/qwc-config-db.git
ALEMBIC_VERSION_DEFAULT=head
POSTGRES_USER_DEFAULT=postgres

[ "$1" == "--help" ] && help

if [ "$QWC_CONFIG_DB_GIT_REPO" == "" ]; then
  QWC_CONFIG_DB_GIT_REPO="$QWC_CONFIG_DB_GIT_REPO_DEFAULT"
fi
if [ "$ALEMBIC_VERSION" == "" ]; then
  ALEMBIC_VERSION="$ALEMBIC_VERSION_DEFAUL"
fi
if [ "$POSTGRES_USER" == "" ]; then
  POSTGRES_USER="$POSTGRES_USER_DEFAULT"
fi

set -e          # stop on error
set -u          # stop on undefined variable
set -o pipefail # stop part of pipeline failing

./install-alembic-and-clone-qwc-config-db.sh "$GIT_REPO"
curl -o /tmp/demo_geodata.gpkg -L https://github.com/pka/mvt-benchmark/raw/master/data/mvtbench.gpkg

POSTGRES_USER=$POSTGRES_USER      ./setup-roles-and-db.sh
ALEMBIC_VERSION=$ALEMBIC_VERSION  ./run-migrations.sh
POSTGRES_USER=$POSTGRES_USER      ./demo-data/setup-demo-data.sh


