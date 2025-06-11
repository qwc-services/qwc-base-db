# A postgres DB with the minimal QWC config DB setup

ARG PG_MAJOR=15
FROM postgres:${PG_MAJOR}

ARG POSTGIS_VERSION=3
ARG PG_SEARCH_VERSION=0.15.25
ENV PGDATA=/var/lib/postgresql/docker
ENV POSTGRES_PASSWORD=

# ENV for qwc-services database roles passwords
ENV QWC_ADMIN_PASSWORD=qwc_admin
ENV QWC_SERVICE_PASSWORD=qwc_service
ENV QWC_SERVICE_WRITE_PASSWORD=qwc_service_write

# Install postgis
RUN \
    apt-get update && \
    apt-get install -y curl postgresql-$PG_MAJOR-postgis-$POSTGIS_VERSION postgresql-$PG_MAJOR-postgis-$POSTGIS_VERSION-scripts && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install pg_search extension
RUN \
    curl -o pg-search.deb -L https://github.com/paradedb/paradedb/releases/download/v${PG_SEARCH_VERSION}/postgresql-${PG_MAJOR}-pg-search_${PG_SEARCH_VERSION}-1PARADEDB-bookworm_amd64.deb && \
    dpkg -i pg-search.deb && \
    echo "shared_preload_libraries='pg_search'" >> /usr/share/postgresql/postgresql.conf.sample && \
    rm pg-search.deb


# Setup database
# script to create DB, roles, grants etc
COPY setup-roles-and-db.sh /docker-entrypoint-initdb.d/0_setup-db.sh
RUN chmod +x /docker-entrypoint-initdb.d/0_setup-db.sh
