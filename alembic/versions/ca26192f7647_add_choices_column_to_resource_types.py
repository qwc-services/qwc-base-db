"""Add choices column to resource_types

Revision ID: ca26192f7647
Revises: b891affa6f74
Create Date: 2026-08-11 14:59:21.178922

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = 'ca26192f7647'
down_revision = 'b891affa6f74'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        ALTER TABLE {schema}.resource_types
          ADD COLUMN choices character varying[] DEFAULT '{{}}';
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        ALTER TABLE {schema}.resource_types DROP COLUMN choices;
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
