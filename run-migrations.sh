#!/bin/sh

until psql service=qwc_configdb -c "select 1" > /dev/null 2>&1; do
  echo "Waiting for postgres server..."
  sleep 1
done

PGSERVICE=qwc_configdb alembic upgrade ${ALEMBIC_VERSION}
