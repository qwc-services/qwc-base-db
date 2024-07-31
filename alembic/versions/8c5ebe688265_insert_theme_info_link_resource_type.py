"""Insert theme_info_link resource type

Revision ID: 8c5ebe688265
Revises: e9c31b610e0a
Create Date: 2020-08-13 11:00:54.732613

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = '8c5ebe688265'
down_revision = 'e9c31b610e0a'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        INSERT INTO {schema}.resource_types (name, description, list_order)
          VALUES (
            'theme_info_link', 'Theme info link',
            (SELECT MAX(list_order) + 1 FROM {schema}.resource_types)
          );
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DELETE FROM {schema}.resource_types WHERE name = 'theme_info_link';
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
