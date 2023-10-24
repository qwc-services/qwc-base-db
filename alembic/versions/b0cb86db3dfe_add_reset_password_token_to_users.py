"""Add reset_password_token to users

Revision ID: b0cb86db3dfe
Revises: 875aa9290232
Create Date: 2018-12-14 09:29:05.469465

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0cb86db3dfe'
down_revision = '875aa9290232'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        ALTER TABLE qwc_config.users
          ADD COLUMN reset_password_token character varying(128);
    """)

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        ALTER TABLE qwc_config.users
          DROP COLUMN reset_password_token;
    """)

    conn = op.get_bind()
    conn.execute(sql)
