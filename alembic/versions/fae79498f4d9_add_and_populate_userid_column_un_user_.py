"""Add and populate userid column un user_visibility_presets

Revision ID: fae79498f4d9
Revises: 323d7de50b07
Create Date: 2026-06-25 12:57:08.344151

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = 'fae79498f4d9'
down_revision = '323d7de50b07'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        ALTER TABLE {schema}.user_visibility_presets
        ADD COLUMN user_id integer;
    """.format(schema=qwc_config_schema))
    conn = op.get_bind()
    conn.execute(sql)

    sql = sa.sql.text("""
        UPDATE {schema}.user_visibility_presets
        SET user_id = users.id
        FROM {schema}.users
        WHERE user_visibility_presets.username = users.name;
    """.format(schema=qwc_config_schema))
    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        ALTER TABLE {schema}.user_visibility_presets
        DROP COLUMN user_id;
    """.format(schema=qwc_config_schema))
    conn = op.get_bind()
    conn.execute(sql)
