"""Create users, groups, roles and relations

Revision ID: 9c671585cfb1
Revises: 
Create Date: 2018-07-03 13:04:20.054758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c671585cfb1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        CREATE TABLE qwc_config.users (
          id serial NOT NULL,
          name character varying NOT NULL,
          description character varying,
          email character varying(120),
          password_hash character varying(128),
          CONSTRAINT users_pk PRIMARY KEY (id),
          CONSTRAINT name_unique UNIQUE (name)
        );

        CREATE TABLE qwc_config.groups (
          id serial NOT NULL,
          name character varying NOT NULL,
          description character varying,
          CONSTRAINT groups_pk PRIMARY KEY (id)
        );

        CREATE TABLE qwc_config.roles (
          id serial NOT NULL,
          name character varying NOT NULL,
          description character varying,
          CONSTRAINT roles_pk PRIMARY KEY (id)
        );

        CREATE TABLE qwc_config.users_roles (
          user_id integer NOT NULL,
          role_id integer NOT NULL,
          CONSTRAINT role_fk FOREIGN KEY (role_id)
              REFERENCES qwc_config.roles (id) MATCH FULL
              ON UPDATE CASCADE ON DELETE RESTRICT,
          CONSTRAINT user_fk FOREIGN KEY (user_id)
              REFERENCES qwc_config.users (id) MATCH FULL
              ON UPDATE CASCADE ON DELETE RESTRICT
        );

        CREATE TABLE qwc_config.groups_users (
          group_id integer NOT NULL,
          user_id integer NOT NULL,
          CONSTRAINT group_fk FOREIGN KEY (group_id)
              REFERENCES qwc_config.groups (id) MATCH FULL
              ON UPDATE CASCADE ON DELETE RESTRICT,
          CONSTRAINT user_fk FOREIGN KEY (user_id)
              REFERENCES qwc_config.users (id) MATCH FULL
              ON UPDATE CASCADE ON DELETE RESTRICT
        );

        CREATE TABLE qwc_config.groups_roles (
          group_id integer NOT NULL,
          role_id integer NOT NULL,
          CONSTRAINT group_fk FOREIGN KEY (group_id)
              REFERENCES qwc_config.groups (id) MATCH FULL
              ON UPDATE CASCADE ON DELETE RESTRICT,
          CONSTRAINT role_fk FOREIGN KEY (role_id)
              REFERENCES qwc_config.roles (id) MATCH FULL
              ON UPDATE CASCADE ON DELETE RESTRICT
        );
    """)

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DROP TABLE qwc_config.users CASCADE;
        DROP TABLE qwc_config.groups CASCADE;
        DROP TABLE qwc_config.roles CASCADE;
        DROP TABLE qwc_config.users_roles CASCADE;
        DROP TABLE qwc_config.groups_users CASCADE;
        DROP TABLE qwc_config.groups_roles CASCADE;
    """)

    conn = op.get_bind()
    conn.execute(sql)
