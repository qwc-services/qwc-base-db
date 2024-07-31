"""Refactor resource_type enum to table

Revision ID: 60c460c23acb
Revises: 5c9dccb16fc2
Create Date: 2018-09-25 15:03:14.447255

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = '60c460c23acb'
down_revision = '5c9dccb16fc2'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        -- create resource_types

        CREATE TABLE {schema}.resource_types (
          name character varying NOT NULL,
          description character varying,
          list_order integer NOT NULL DEFAULT 0,
          CONSTRAINT resource_types_pk PRIMARY KEY (name)
        );

        WITH types AS (
          SELECT name::text, list_order::integer
          FROM unnest(
            enum_range(NULL::{schema}.resource_type)
          ) WITH ORDINALITY AS t(name, list_order)
        )
        INSERT INTO {schema}.resource_types
          (name, description, list_order)
          SELECT name, initcap(name), list_order FROM types;

        -- refactor resources.type from enum to FK on resource_types

        ALTER TABLE {schema}.resources
          ALTER COLUMN type TYPE character varying
          USING type::text;

        ALTER TABLE {schema}.resources
          ADD CONSTRAINT type_fk FOREIGN KEY (type)
            REFERENCES {schema}.resource_types (name) MATCH FULL
            ON UPDATE CASCADE ON DELETE RESTRICT;

        -- cleanup

        DROP TYPE {schema}.resource_type;
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        -- recreate enum

        CREATE TYPE {schema}.resource_type AS
          ENUM ('map', 'layer', 'attribute', 'data');

        -- revert resources.type from FK on resource_types to enum

        ALTER TABLE {schema}.resources
          DROP CONSTRAINT type_fk;

        ALTER TABLE {schema}.resources
          ALTER COLUMN type TYPE {schema}.resource_type
          USING type::{schema}.resource_type;

        -- cleanup

        DROP TABLE {schema}.resource_types CASCADE;
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
