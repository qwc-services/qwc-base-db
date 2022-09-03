# QWC Services base DB
#
# This is mostly the same as setup-external-db.sh
#
#                     PLEASE KEEP IN SYNC
#
# container ready to serve data from /data volume:
#
# - includes postgres server with postgis
# - *on start* will check whether migration is needed.
#   If migration is needed:
#   - will set up config-db
#
# Please set ALEMBIC_VERSION to a specific commit hash
# in the docker image runtime environment, if you want
# to check out and run a different version of
# qwc-config-db migrations than those from `head`.
# See the `run-migrations.sh`.

FROM postgres:13

ENV DEBIAN_FRONTEND=noninteractive

ARG PG_MAJOR=13
ARG POSTGIS_VERSION=3

ARG GIT_REPO=https://github.com/qwc-services/qwc-config-db.git

ENV PGSERVICEFILE=/tmp/.pg_service.conf

COPY install-postgis.sh install-alembic-and-clone-qwc-config-db.sh /usr/local/bin/
RUN  cd /usr/local/bin && \
     chmod +x install-postgis.sh install-alembic-and-clone-qwc-config-db.sh

RUN \
    export PATH=/usr/local/bin:/usr/bin:/bin && \
    apt-get update && \
    apt-get upgrade -y && \
    /usr/local/bin/install-postgis.sh $PG_MAJOR $POSTGIS_VERSION && \
    /usr/local/bin/install-alembic-and-clone-qwc-config-db.sh $GIT_REPO && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

#RUN localedef -i de_CH -c -f UTF-8 -A /usr/share/locale/locale.alias de_CH.UTF-8
#ENV LANG de_CH.utf8


# setup database
# script to create DB, roles, grants etc
COPY setup-roles-and-db.sh /docker-entrypoint-initdb.d/0_setup-db.sh

# script to create tables
COPY run-migrations.sh /docker-entrypoint-initdb.d/1_run-migrations.sh

RUN chmod +x /docker-entrypoint-initdb.d/*.sh
RUN cp -a /usr/local/bin/docker-entrypoint.sh /tmp/docker-entrypoint.sh

ENV PGDATA /var/lib/postgresql/docker
ENV POSTGRES_PASSWORD U6ZqsEdBmrER
