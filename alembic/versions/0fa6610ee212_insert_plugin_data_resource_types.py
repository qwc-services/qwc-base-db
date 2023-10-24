"""Insert plugin data resource types

Revision ID: 0fa6610ee212
Revises: 8c5ebe688265
Create Date: 2020-08-13 11:06:10.456910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fa6610ee212'
down_revision = '8c5ebe688265'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        INSERT INTO qwc_config.resource_types (name, description, list_order)
          VALUES (
            'plugin', 'Plugin',
            (SELECT MAX(list_order) + 1 FROM qwc_config.resource_types)
          );
        INSERT INTO qwc_config.resource_types (name, description, list_order)
          VALUES (
            'plugin_data', 'Plugin data',
            (SELECT MAX(list_order) + 1 FROM qwc_config.resource_types)
          );
    """)

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DELETE FROM qwc_config.resource_types WHERE name = 'plugin';
        DELETE FROM qwc_config.resource_types WHERE name = 'plugin_data';
    """)

    conn = op.get_bind()
    conn.execute(sql)
