"""Add permitted_group to permalinks table

Revision ID: bd84e7f12b72
Revises: b4b1291b2628
Create Date: 2025-03-18 17:57:03.630566

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = 'bd84e7f12b72'
down_revision = 'b4b1291b2628'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        ALTER TABLE {schema}.permalinks
        ADD COLUMN permitted_group text;
    """.format(schema=qwc_config_schema))
    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        ALTER TABLE {schema}.user_infos
        DROP COLUMN permitted_group;
    """.format(schema=qwc_config_schema))
    conn = op.get_bind()
    conn.execute(sql)
