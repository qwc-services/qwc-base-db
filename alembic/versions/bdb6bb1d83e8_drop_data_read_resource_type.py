"""Drop Data (Read) resource type

Revision ID: bdb6bb1d83e8
Revises: 973e774e182a
Create Date: 2025-08-05 10:45:22.241833

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = 'bdb6bb1d83e8'
down_revision = '973e774e182a'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        UPDATE {schema}.resources SET type = 'data' WHERE type = 'data_read';
        DELETE FROM {schema}.resource_types WHERE name = 'data_read';
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        INSERT INTO {schema}.resource_types (name, description, list_order)
          VALUES (
            'data_read', 'Data (read)',
            (SELECT MAX(list_order) + 1 FROM {schema}.resource_types)
          );
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
