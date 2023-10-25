"""drop not null constrains on user_infos fields

Revision ID: d397557cf130
Revises: 85d1c50359ad
Create Date: 2023-10-25 13:45:55.692935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd397557cf130'
down_revision = '85d1c50359ad'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        ALTER TABLE qwc_config.user_infos
        ALTER COLUMN surname
        DROP NOT NULL;
        ALTER TABLE qwc_config.user_infos
        ALTER COLUMN first_name
        DROP NOT NULL;
    """)
    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        ALTER TABLE qwc_config.user_infos
        ALTER COLUMN surname
        NOT NULL;
        ALTER TABLE qwc_config.user_infos
        ALTER COLUMN first_name
        NOT NULL;
    """)
    conn = op.get_bind()
    conn.execute(sql)
