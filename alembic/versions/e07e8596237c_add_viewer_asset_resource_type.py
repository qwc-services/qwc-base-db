"""Add Viewer asset resource type

Revision ID: e07e8596237c
Revises: 7597605b586e
Create Date: 2025-09-02 18:57:28.398643

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = 'e07e8596237c'
down_revision = '7597605b586e'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        INSERT INTO {schema}.resource_types (name, description, list_order)
          VALUES (
            'viewer_asset', 'Viewer asset',
            (SELECT MAX(list_order) + 1 FROM {schema}.resource_types)
          );
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DELETE FROM {schema}.resource_types WHERE name = 'viewer_asset';
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
