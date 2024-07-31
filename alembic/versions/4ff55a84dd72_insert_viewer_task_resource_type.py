"""Insert viewer_task resource type

Revision ID: 4ff55a84dd72
Revises: a793057bbf20
Create Date: 2019-01-09 16:40:45.622573

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = '4ff55a84dd72'
down_revision = 'a793057bbf20'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        INSERT INTO {schema}.resource_types (name, description, list_order)
          VALUES (
            'viewer_task', 'Viewer task',
            (SELECT MAX(list_order) + 1 FROM {schema}.resource_types)
          );
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DELETE FROM {schema}.resource_types WHERE name = 'viewer_task';
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
