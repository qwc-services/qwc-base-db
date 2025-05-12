"""Add 3dtiles resource type

Revision ID: f59f5c7f2afa
Revises: aa8bc8dfaa3d
Create Date: 2025-05-12 15:01:04.507130

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = 'f59f5c7f2afa'
down_revision = 'aa8bc8dfaa3d'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        INSERT INTO {schema}.resource_types (name, description, list_order)
          VALUES (
            'tileset3d', '3D Tiles Tileset',
            (SELECT MAX(list_order) + 1 FROM {schema}.resource_types)
          );
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DELETE FROM {schema}.resource_types WHERE name = 'tileset3d';
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
