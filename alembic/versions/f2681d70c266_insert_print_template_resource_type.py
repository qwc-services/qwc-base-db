"""Insert print template resource type

Revision ID: f2681d70c266
Revises: 916ed45fa0ba
Create Date: 2018-12-12 15:45:01.694680

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = 'f2681d70c266'
down_revision = '916ed45fa0ba'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        INSERT INTO {schema}.resource_types (name, description, list_order)
          VALUES (
            'print_template', 'Print template',
            (SELECT MAX(list_order) + 1 FROM {schema}.resource_types)
          );
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DELETE FROM {schema}.resource_types WHERE name = 'print_template';
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
