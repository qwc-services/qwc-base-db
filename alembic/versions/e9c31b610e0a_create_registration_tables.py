"""Create registration tables

Add tables for registrable groups and registration requests.

Revision ID: e9c31b610e0a
Revises: 90b3b4fbc8f6
Create Date: 2019-02-18 13:00:54.485628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9c31b610e0a'
down_revision = '90b3b4fbc8f6'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        CREATE TABLE qwc_config.registrable_groups (
          id serial NOT NULL,
          group_id integer NOT NULL,
          title character varying NOT NULL,
          description character varying,
          CONSTRAINT registrable_groups_pk PRIMARY KEY (id),
          CONSTRAINT group_fk FOREIGN KEY (group_id)
              REFERENCES qwc_config.groups (id) MATCH FULL
              ON UPDATE CASCADE ON DELETE RESTRICT
        );

        CREATE TABLE qwc_config.registration_requests (
          id serial NOT NULL,
          user_id integer NOT NULL,
          registrable_group_id integer NOT NULL,
          unsubscribe boolean NOT NULL DEFAULT false,
          pending boolean NOT NULL DEFAULT true,
          accepted boolean,
          created_at timestamp without time zone NOT NULL,
          CONSTRAINT registration_requests_pk PRIMARY KEY (id),
          CONSTRAINT user_fk FOREIGN KEY (user_id)
              REFERENCES qwc_config.users (id) MATCH FULL
              ON UPDATE CASCADE ON DELETE RESTRICT,
          CONSTRAINT registrable_group_fk FOREIGN KEY (registrable_group_id)
              REFERENCES qwc_config.registrable_groups (id) MATCH FULL
              ON UPDATE CASCADE ON DELETE RESTRICT
        );
    """)

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DROP TABLE qwc_config.registration_requests CASCADE;
        DROP TABLE qwc_config.registrable_groups CASCADE;
    """)

    conn = op.get_bind()
    conn.execute(sql)
