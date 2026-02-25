"""Rename tileset3d resource to object3d

Revision ID: 76bd94175ce4
Revises: 6e095634bbeb
Create Date: 2026-02-24 19:59:44.694869

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = '76bd94175ce4'
down_revision = '6e095634bbeb'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        UPDATE {schema}.resource_types
        SET name='object3d', description='3D Object'
        WHERE name='tileset3d';
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        UPDATE {schema}.resource_types
        SET name='tileset3d', description='3D Tiles Tileset'
        WHERE name='object3d';
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
