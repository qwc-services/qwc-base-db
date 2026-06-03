"""Add theme_id to user_bookmarks and user_visibility_presets

Revision ID: 323d7de50b07
Revises: 3d9a7b922542
Create Date: 2026-06-03 15:38:45.460583

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = '323d7de50b07'
down_revision = '3d9a7b922542'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        ALTER TABLE {schema}.user_bookmarks
        ADD COLUMN theme_id text;
        ALTER TABLE {schema}.user_visibility_presets
        ADD COLUMN theme_id text;
    """.format(schema=qwc_config_schema))
    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        ALTER TABLE {schema}.user_bookmarks
        DROP COLUMN theme_id;
        ALTER TABLE {schema}.user_visibility_presets
        DROP COLUMN theme_id;
    """.format(schema=qwc_config_schema))
    conn = op.get_bind()
    conn.execute(sql)
