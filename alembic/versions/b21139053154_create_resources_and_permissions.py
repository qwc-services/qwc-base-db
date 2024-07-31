"""Create resources and permissions

Revision ID: b21139053154
Revises: 9c671585cfb1
Create Date: 2018-07-03 13:09:23.087429

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = 'b21139053154'
down_revision = '9c671585cfb1'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        CREATE TYPE {schema}.resource_type AS
          ENUM ('map', 'layer', 'attribute');

        CREATE TABLE {schema}.resources (
          id serial NOT NULL,
          parent_id integer,
          type {schema}.resource_type NOT NULL,
          name character varying NOT NULL,
          CONSTRAINT resources_pk PRIMARY KEY (id),
          CONSTRAINT parent_fk FOREIGN KEY (parent_id)
              REFERENCES {schema}.resources (id) MATCH FULL
              ON UPDATE CASCADE ON DELETE RESTRICT
        );

        CREATE TABLE {schema}.permissions (
          id serial NOT NULL,
          role_id integer NOT NULL,
          resource_id integer NOT NULL,
          priority integer NOT NULL DEFAULT 0,
          write boolean NOT NULL DEFAULT FALSE,
          CONSTRAINT permissions_pk PRIMARY KEY (id),
          CONSTRAINT role_fk FOREIGN KEY (role_id)
              REFERENCES {schema}.roles (id) MATCH FULL
              ON UPDATE CASCADE ON DELETE RESTRICT,
          CONSTRAINT resource_fk FOREIGN KEY (resource_id)
              REFERENCES {schema}.resources (id) MATCH FULL
              ON UPDATE CASCADE ON DELETE RESTRICT
        );
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DROP TABLE {schema}.resources CASCADE;
        DROP TABLE {schema}.permissions CASCADE;
        DROP TYPE {schema}.resource_type;
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
