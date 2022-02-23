QWC DB setup
============

This repository is concerned with configuring a postgres DB,
so that it can be used by QWC.

The software herein has two basic targets:

* creating a basic Docker container, containing
  a postgres server, postgis and demo data, that can
  be used if wanted.

  The https://github.com/qwc-services/qwc-demo-db repository
  uses this to create another container with a ready to
  use database filled with demo data for easy trying out QWC2.

* providing a script that will set up an external postgres
  server and add demo data so that it can be used with QWC2.

TODO:
* re-add badges
