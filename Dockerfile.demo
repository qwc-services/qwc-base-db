# QWC Services DB with demo data
#
# This is mostly the same as Dockerfile.qwc-base-db and setup-external-db.sh
#
#                     PLEASE KEEP IN SYNC
#
# self contained container:
# - includes postgres server with postgis
# - config-db is set up
# - demo data are in the DB
#
FROM qwc-base-db:13

# Set ALEMBIC_VERSION to force git pull of qwc-config-db repo
# used by run-migrations.sh script
ARG ALEMBIC_VERSION=head

# After running all the /docker-entrypoint-initdb.d scripts we just
# want to terminate at build time and *not* to run postgres.
# Thus we patch the docker-entrypoint.sh script to comment the exec out.
RUN sed --in-place 's/^\t*exec "$@"//' /tmp/docker-entrypoint.sh

# the following will start postgres and run the above added scripts
# under /docker-entrypoint-initdb.d
RUN gosu postgres bash /tmp/docker-entrypoint.sh postgres
