#!/bin/bash
set -e

# run migrations from qwc-config-db
cd /tmp/qwc-config-db/
source .venv/bin/activate
PGSERVICE=qwc_configdb alembic upgrade ${ALEMBIC_VERSION:-head}
