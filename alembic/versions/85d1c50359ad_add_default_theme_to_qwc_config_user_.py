"""add default_url_params to {schema}.user_infos

Revision ID: 85d1c50359ad
Revises: 46eeef9d6787
Create Date: 2023-10-25 12:17:44.364919

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = '85d1c50359ad'
down_revision = '46eeef9d6787'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        ALTER TABLE {schema}.user_infos
        ADD COLUMN default_url_params character varying;
    """.format(schema=qwc_config_schema))
    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        ALTER TABLE {schema}.user_infos
        DROP COLUMN default_url_params;
    """.format(schema=qwc_config_schema))
    conn = op.get_bind()
    conn.execute(sql)
