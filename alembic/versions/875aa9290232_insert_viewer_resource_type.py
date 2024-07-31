"""Insert viewer resource type

Revision ID: 875aa9290232
Revises: f2681d70c266
Create Date: 2018-12-13 16:01:28.360306

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = '875aa9290232'
down_revision = 'f2681d70c266'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        INSERT INTO {schema}.resource_types (name, description, list_order)
          VALUES (
            'viewer', 'Viewer',
            (SELECT MAX(list_order) + 1 FROM {schema}.resource_types)
          );
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DELETE FROM {schema}.resource_types WHERE name = 'viewer';
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
