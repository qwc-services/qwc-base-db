"""Remove unused viewer resource type

Revision ID: 7597605b586e
Revises: bdb6bb1d83e8
Create Date: 2025-09-02 18:31:27.949203

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = '7597605b586e'
down_revision = 'bdb6bb1d83e8'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        UPDATE {schema}.resources SET type = 'viewer_task' WHERE type = 'viewer';
        DELETE FROM {schema}.resource_types WHERE name = 'viewer';
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        INSERT INTO {schema}.resource_types (name, description, list_order)
          VALUES (
            'viewer', 'Viewer',
            (SELECT MAX(list_order) + 1 FROM {schema}.resource_types)
          );
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
