#!/bin/bash
set -e

qwc_config_schema=${QWC_CONFIG_SCHEMA:-qwc_config}

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
  CREATE ROLE qgis_server LOGIN PASSWORD '$QGIS_SERVER_PASSWORD';
  CREATE ROLE qwc_admin LOGIN PASSWORD '$QWC_ADMIN_PASSWORD';
  CREATE ROLE qwc_service LOGIN PASSWORD '$QWC_SERVICE_PASSWORD';
  CREATE ROLE qwc_service_write LOGIN PASSWORD '$QWC_SERVICE_WRITE_PASSWORD';

  CREATE DATABASE qwc_services;
  COMMENT ON DATABASE qwc_services IS 'DB for qwc-services';
EOSQL

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" -d qwc_services <<-EOSQL
  CREATE SCHEMA ${qwc_config_schema} AUTHORIZATION qwc_admin;
  COMMENT ON SCHEMA ${qwc_config_schema} IS 'ConfigDB for qwc-services';
EOSQL

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" -d qwc_services <<-EOSQL
  CREATE EXTENSION postgis;
  GRANT SELECT ON TABLE geometry_columns TO PUBLIC;
  GRANT SELECT ON TABLE geography_columns TO PUBLIC;
  GRANT SELECT ON TABLE spatial_ref_sys TO PUBLIC;
EOSQL
