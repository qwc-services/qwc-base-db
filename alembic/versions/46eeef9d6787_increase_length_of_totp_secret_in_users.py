"""Increase length of TOTP secret in users

Revision ID: 46eeef9d6787
Revises: ad5e7b02469a
Create Date: 2022-04-20 13:30:44.304793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46eeef9d6787'
down_revision = 'ad5e7b02469a'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        ALTER TABLE qwc_config.users
          ALTER COLUMN totp_secret TYPE character varying(128);
    """)

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        ALTER TABLE qwc_config.users
          ALTER COLUMN totp_secret TYPE character varying(16);
    """)

    conn = op.get_bind()
    conn.execute(sql)
