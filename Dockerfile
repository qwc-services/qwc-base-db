# A postgres DB with the minimal QWC config DB setup

FROM postgres:15

ENV PGDATA=/var/lib/postgresql/docker
ENV POSTGRES_PASSWORD=

ARG PG_MAJOR=15
ARG POSTGIS_VERSION=3

# Install postgis
RUN \
    apt-get update && \
    apt-get install -y curl postgresql-$PG_MAJOR-postgis-$POSTGIS_VERSION postgresql-$PG_MAJOR-postgis-$POSTGIS_VERSION-scripts && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Setup database
# script to create DB, roles, grants etc
COPY setup-roles-and-db.sh /docker-entrypoint-initdb.d/0_setup-db.sh
RUN chmod +x /docker-entrypoint-initdb.d/0_setup-db.sh
