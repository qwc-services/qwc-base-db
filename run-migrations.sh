#!/bin/sh

until psql service=$PGSERVICE -c "select 1" > /dev/null 2>&1; do
  echo "Waiting for postgres server..."
  sleep 1
done

current_version=$(alembic current)
echo "Current version: ${current_version}"


alembic upgrade ${ALEMBIC_VERSION}

if [ -z "$current_version" ] && [ -d "/tmp/extra-init.d" ]; then
  echo "Executing scripts in /tmp/extra-init.d..."
  for script in /tmp/extra-init.d/*; do
    if [ -f "$script" ] && [ -x "$script" ]; then
      echo "Running $script..."
      "$script"
    elif [ -f "$script" ]; then
      echo "Running $script with sh..."
      sh "$script"
    fi
  done
fi
