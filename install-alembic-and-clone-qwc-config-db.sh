#!/bin/bash

help() {
   echo 'usage: install-alembic-and-clone-qwc-config-db QWC_CONFIG_DB_GIT_REPO'
   echo '       install-alembic-and-clone-qwc-config-db -alembic --help'
   echo
   exit 1
}

[ "$1" == "--help" ] || [ "$1" == "" ] && help

set -e # stop on error

QWC_CONFIG_DB_GIT_REPO="$1"
QWC_CONFIG_DB_DEST="$2"

apt-get install -y ca-certificates tmux screen curl less \
                   git python3-pip python3-psycopg2 python3-venv libpq-dev gdal-bin

# get qwc-config-db for migrations
cd /tmp/ && git clone $QWC_CONFIG_DB_GIT_REPO qwc-config-db
cd /tmp/qwc-config-db/ && git pull
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install --no-cache-dir -r /tmp/qwc-config-db/requirements.txt

