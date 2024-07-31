"""Add reset_password_token to users

Revision ID: b0cb86db3dfe
Revises: 875aa9290232
Create Date: 2018-12-14 09:29:05.469465

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = 'b0cb86db3dfe'
down_revision = '875aa9290232'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        ALTER TABLE {schema}.users
          ADD COLUMN reset_password_token character varying(128);
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        ALTER TABLE {schema}.users
          DROP COLUMN reset_password_token;
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
