"""add expires column to permalinks table

Revision ID: 0307976d3d52
Revises: 85d1c50359ad
Create Date: 2023-10-26 19:18:52.896721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0307976d3d52'
down_revision = '85d1c50359ad'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        ALTER TABLE qwc_config.permalinks
        ADD COLUMN expires date;
    """)
    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        ALTER TABLE qwc_config.user_infos
        DROP COLUMN expires;
    """)
    conn = op.get_bind()
    conn.execute(sql)
