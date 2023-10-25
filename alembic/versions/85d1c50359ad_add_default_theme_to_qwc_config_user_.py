"""add default_url_params to qwc_config.user_infos

Revision ID: 85d1c50359ad
Revises: 46eeef9d6787
Create Date: 2023-10-25 12:17:44.364919

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85d1c50359ad'
down_revision = '46eeef9d6787'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        ALTER TABLE qwc_config.user_infos
        ADD COLUMN default_url_params character varying;
    """)
    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        ALTER TABLE qwc_config.user_infos
        DROP COLUMN default_url_params;
    """)
    conn = op.get_bind()
    conn.execute(sql)
