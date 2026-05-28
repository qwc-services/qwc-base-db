"""Add default map resource type

Revision ID: 417fb25a35fd
Revises: 76bd94175ce4
Create Date: 2026-05-28 10:32:06.351047

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = '417fb25a35fd'
down_revision = '76bd94175ce4'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        INSERT INTO {schema}.resource_types (name, description, list_order)
          VALUES (
            'default_theme', 'Default Theme',
            (SELECT MAX(list_order) + 1 FROM {schema}.resource_types)
          );
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DELETE FROM {schema}.resource_types WHERE name = 'default_theme';
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
