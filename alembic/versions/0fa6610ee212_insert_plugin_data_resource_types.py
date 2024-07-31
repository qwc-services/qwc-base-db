"""Insert plugin data resource types

Revision ID: 0fa6610ee212
Revises: 8c5ebe688265
Create Date: 2020-08-13 11:06:10.456910

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = '0fa6610ee212'
down_revision = '8c5ebe688265'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        INSERT INTO {schema}.resource_types (name, description, list_order)
          VALUES (
            'plugin', 'Plugin',
            (SELECT MAX(list_order) + 1 FROM {schema}.resource_types)
          );
        INSERT INTO {schema}.resource_types (name, description, list_order)
          VALUES (
            'plugin_data', 'Plugin data',
            (SELECT MAX(list_order) + 1 FROM {schema}.resource_types)
          );
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DELETE FROM {schema}.resource_types WHERE name = 'plugin';
        DELETE FROM {schema}.resource_types WHERE name = 'plugin_data';
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
