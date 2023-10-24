"""Refactor resource_type enum to table

Revision ID: 60c460c23acb
Revises: 5c9dccb16fc2
Create Date: 2018-09-25 15:03:14.447255

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60c460c23acb'
down_revision = '5c9dccb16fc2'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        -- create resource_types

        CREATE TABLE qwc_config.resource_types (
          name character varying NOT NULL,
          description character varying,
          list_order integer NOT NULL DEFAULT 0,
          CONSTRAINT resource_types_pk PRIMARY KEY (name)
        );

        WITH types AS (
          SELECT name::text, list_order::integer
          FROM unnest(
            enum_range(NULL::qwc_config.resource_type)
          ) WITH ORDINALITY AS t(name, list_order)
        )
        INSERT INTO qwc_config.resource_types
          (name, description, list_order)
          SELECT name, initcap(name), list_order FROM types;

        -- refactor resources.type from enum to FK on resource_types

        ALTER TABLE qwc_config.resources
          ALTER COLUMN type TYPE character varying
          USING type::text;

        ALTER TABLE qwc_config.resources
          ADD CONSTRAINT type_fk FOREIGN KEY (type)
            REFERENCES qwc_config.resource_types (name) MATCH FULL
            ON UPDATE CASCADE ON DELETE RESTRICT;

        -- cleanup

        DROP TYPE qwc_config.resource_type;
    """)

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        -- recreate enum

        CREATE TYPE qwc_config.resource_type AS
          ENUM ('map', 'layer', 'attribute', 'data');

        -- revert resources.type from FK on resource_types to enum

        ALTER TABLE qwc_config.resources
          DROP CONSTRAINT type_fk;

        ALTER TABLE qwc_config.resources
          ALTER COLUMN type TYPE qwc_config.resource_type
          USING type::qwc_config.resource_type;

        -- cleanup

        DROP TABLE qwc_config.resource_types CASCADE;
    """)

    conn = op.get_bind()
    conn.execute(sql)
