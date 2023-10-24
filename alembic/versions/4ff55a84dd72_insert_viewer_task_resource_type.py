"""Insert viewer_task resource type

Revision ID: 4ff55a84dd72
Revises: a793057bbf20
Create Date: 2019-01-09 16:40:45.622573

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ff55a84dd72'
down_revision = 'a793057bbf20'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        INSERT INTO qwc_config.resource_types (name, description, list_order)
          VALUES (
            'viewer_task', 'Viewer task',
            (SELECT MAX(list_order) + 1 FROM qwc_config.resource_types)
          );
    """)

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DELETE FROM qwc_config.resource_types WHERE name = 'viewer_task';
    """)

    conn = op.get_bind()
    conn.execute(sql)
