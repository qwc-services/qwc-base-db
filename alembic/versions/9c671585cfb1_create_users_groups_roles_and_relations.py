"""Create users, groups, roles and relations

Revision ID: 9c671585cfb1
Revises: 
Create Date: 2018-07-03 13:04:20.054758

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = '9c671585cfb1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        CREATE TABLE {schema}.users (
          id serial NOT NULL,
          name character varying NOT NULL,
          description character varying,
          email character varying(120),
          password_hash character varying(128),
          CONSTRAINT users_pk PRIMARY KEY (id),
          CONSTRAINT name_unique UNIQUE (name)
        );

        CREATE TABLE {schema}.groups (
          id serial NOT NULL,
          name character varying NOT NULL,
          description character varying,
          CONSTRAINT groups_pk PRIMARY KEY (id)
        );

        CREATE TABLE {schema}.roles (
          id serial NOT NULL,
          name character varying NOT NULL,
          description character varying,
          CONSTRAINT roles_pk PRIMARY KEY (id)
        );

        CREATE TABLE {schema}.users_roles (
          user_id integer NOT NULL,
          role_id integer NOT NULL,
          CONSTRAINT role_fk FOREIGN KEY (role_id)
              REFERENCES {schema}.roles (id) MATCH FULL
              ON UPDATE CASCADE ON DELETE RESTRICT,
          CONSTRAINT user_fk FOREIGN KEY (user_id)
              REFERENCES {schema}.users (id) MATCH FULL
              ON UPDATE CASCADE ON DELETE RESTRICT
        );

        CREATE TABLE {schema}.groups_users (
          group_id integer NOT NULL,
          user_id integer NOT NULL,
          CONSTRAINT group_fk FOREIGN KEY (group_id)
              REFERENCES {schema}.groups (id) MATCH FULL
              ON UPDATE CASCADE ON DELETE RESTRICT,
          CONSTRAINT user_fk FOREIGN KEY (user_id)
              REFERENCES {schema}.users (id) MATCH FULL
              ON UPDATE CASCADE ON DELETE RESTRICT
        );

        CREATE TABLE {schema}.groups_roles (
          group_id integer NOT NULL,
          role_id integer NOT NULL,
          CONSTRAINT group_fk FOREIGN KEY (group_id)
              REFERENCES {schema}.groups (id) MATCH FULL
              ON UPDATE CASCADE ON DELETE RESTRICT,
          CONSTRAINT role_fk FOREIGN KEY (role_id)
              REFERENCES {schema}.roles (id) MATCH FULL
              ON UPDATE CASCADE ON DELETE RESTRICT
        );
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DROP TABLE {schema}.users CASCADE;
        DROP TABLE {schema}.groups CASCADE;
        DROP TABLE {schema}.roles CASCADE;
        DROP TABLE {schema}.users_roles CASCADE;
        DROP TABLE {schema}.groups_users CASCADE;
        DROP TABLE {schema}.groups_roles CASCADE;
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
