"""Add mapinfo resource type

Revision ID: 4aa92e9eb2c0
Revises: e07e8596237c
Create Date: 2025-09-29 18:50:35.008753

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = '4aa92e9eb2c0'
down_revision = 'e07e8596237c'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        INSERT INTO {schema}.resource_types (name, description, list_order)
          VALUES (
            'mapinfo_query', 'Map info query',
            (SELECT MAX(list_order) + 1 FROM {schema}.resource_types)
          );
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DELETE FROM {schema}.resource_types WHERE name = 'mapinfo_query';
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
