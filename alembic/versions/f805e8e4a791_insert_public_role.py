"""Insert public role

Revision ID: f805e8e4a791
Revises: b21139053154
Create Date: 2018-07-03 13:11:00.253559

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f805e8e4a791'
down_revision = 'b21139053154'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        INSERT INTO qwc_config.roles (name, description)
          VALUES ('public', 'Public role');
    """)

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DELETE FROM qwc_config.roles WHERE name = 'public';
    """)

    conn = op.get_bind()
    conn.execute(sql)
