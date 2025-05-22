# A postgres DB with the minimal QWC config DB setup

ARG PG_MAJOR=15
FROM postgres:${PG_MAJOR}

ARG POSTGIS_VERSION=3
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

# Setup database
# script to create DB, roles, grants etc
COPY setup-roles-and-db.sh /docker-entrypoint-initdb.d/0_setup-db.sh
RUN chmod +x /docker-entrypoint-initdb.d/0_setup-db.sh
