#!/bin/sh

until psql service=$PGSERVICE -c "select 1" > /dev/null 2>&1; do
  echo "Waiting for postgres server..."
  sleep 1
done

alembic upgrade ${ALEMBIC_VERSION}
