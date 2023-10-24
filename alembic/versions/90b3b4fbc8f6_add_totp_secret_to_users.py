"""Add TOTP secret to users

Revision ID: 90b3b4fbc8f6
Revises: 4ff55a84dd72
Create Date: 2019-02-01 13:46:48.426617

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90b3b4fbc8f6'
down_revision = '4ff55a84dd72'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        ALTER TABLE qwc_config.users
          ADD COLUMN totp_secret character varying(16);
    """)

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        ALTER TABLE qwc_config.users
          DROP COLUMN totp_secret;
    """)

    conn = op.get_bind()
    conn.execute(sql)
