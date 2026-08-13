"""Add capabilities resource type

Revision ID: bb61518dc5ad
Revises: ca26192f7647
Create Date: 2026-08-11 15:11:17.249203

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = 'bb61518dc5ad'
down_revision = 'ca26192f7647'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        INSERT INTO {schema}.resource_types (name, description, list_order, choices)
          VALUES (
            'capabilities', 'Capabilities',
            (SELECT MAX(list_order) + 1 FROM {schema}.resource_types),
            ARRAY['public_bookmarks']
          );
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DELETE FROM {schema}.resource_types WHERE name = 'capabilities';
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
