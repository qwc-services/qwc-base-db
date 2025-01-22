"""Add dataproduct resource

Revision ID: b4b1291b2628
Revises: 59709e421270
Create Date: 2025-01-22 19:16:12.075431

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = 'b4b1291b2628'
down_revision = '59709e421270'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        INSERT INTO {schema}.resource_types (name, description, list_order)
          VALUES (
            'dataproduct', 'Dataproduct',
            (SELECT MAX(list_order) + 1 FROM {schema}.resource_types)
          );
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DELETE FROM {schema}.resource_types WHERE name = 'dataproduct';
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
