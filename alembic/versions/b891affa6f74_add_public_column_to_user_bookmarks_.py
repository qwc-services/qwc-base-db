"""Add public column to user_bookmarks table

Revision ID: b891affa6f74
Revises: fae79498f4d9
Create Date: 2026-08-11 10:15:24.831181

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = 'b891affa6f74'
down_revision = 'fae79498f4d9'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        ALTER TABLE {schema}.user_bookmarks
        ADD COLUMN public boolean DEFAULT false;
        ALTER TABLE {schema}.user_visibility_presets
        ADD COLUMN public boolean DEFAULT false;
    """.format(schema=qwc_config_schema))
    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        ALTER TABLE {schema}.user_bookmarks
        DROP COLUMN public;
        ALTER TABLE {schema}.user_visibility_presets
        DROP COLUMN public;
    """.format(schema=qwc_config_schema))
    conn = op.get_bind()
    conn.execute(sql)
