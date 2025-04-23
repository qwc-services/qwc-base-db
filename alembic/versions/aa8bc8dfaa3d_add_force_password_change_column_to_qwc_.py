"""Add force_password_change column to qwc_config.users

Revision ID: aa8bc8dfaa3d
Revises: bd84e7f12b72
Create Date: 2025-04-23 09:11:17.278099

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = 'aa8bc8dfaa3d'
down_revision = 'bd84e7f12b72'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        ALTER TABLE {schema}.users
        ADD COLUMN force_password_change boolean;
    """.format(schema=qwc_config_schema))
    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        ALTER TABLE {schema}.users
        DROP COLUMN force_password_change;
    """.format(schema=qwc_config_schema))
    conn = op.get_bind()
    conn.execute(sql)
