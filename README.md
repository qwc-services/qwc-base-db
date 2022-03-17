[![CI](https://github.com/qwc-services/qwc-db-setup/actions/workflows/qwc-base-db.yml/badge.svg)](https://github.com/qwc-services/qwc-db-setup/actions)
[![docker](https://img.shields.io/docker/v/sourcepole/qwc-base-db?label=qwc-demo-db%20image&sort=semver)](https://hub.docker.com/r/sourcepole/qwc-base-db)

QWC DB setup
============

This repository is concerned with configuring a postgres DB,
so that it can be used by QWC.

The image contains the postgres server, the postgis extension,
and scripts to set up the `qwc_configdb` configuration database
and scripts to insert the demo data.



Usage
-----

### The Docker container image

The qwc-base-db Docker image is based on the
[official Postgres Docker container image](https://hub.docker.com/_/postgres/).
The mechanisms discussed below are based on those
provided by the Postgres Docker image. Please
see at the mentioned link.

The qwc-base-db Docker container image meant to be used like this:

    $ cat docker-compose.yml
    version: '2.1'
    services:
      qwc-postgis:
        image: sourcepole/qwc-base-db
        environment:
          - ALEMBIC_VERSION=head
          - PGDATA=/var/lib/postgresql/data/pgdata
        healthcheck:
          test: ["CMD-SHELL", "pg_isready -U postgres"]
          interval: 10s
        ports:
         - "0.0.0.0:5432:5432"
        volumes:
          - ./volumes/postgres-data:/var/lib/postgresql/data
    [...]

Upon start, the container will check whether `/var/lib/postgresql/data`
is empty.

#### starting with an empty `/var/lib/postgresql/data` volume

If `/var/lib/postgresql/data` is empty, then postgres will initialize it
and execute scripts under `/docker-entrypoint-initdb.d` that will set up
a `qwc_demo` DB and fill it with demo data.

#### starting with an non-empty `/var/lib/postgresql/data` volume

If `/var/lib/postgresql/data` is *NOT* empty, such as when:

* the container had already been started in the past and had already
  initialized the the DB inside the provided volume or

* the admin has attached a volume to the container that had some
  other postgres database in it

then postgres will just start and try to use the data that is already
under `/var/lib/postgresql/data`.
