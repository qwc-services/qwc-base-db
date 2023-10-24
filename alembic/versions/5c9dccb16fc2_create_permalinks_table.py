"""Create permalinks table

Revision ID: 5c9dccb16fc2
Revises: 217f272b9c26
Create Date: 2018-09-06 10:48:08.151209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c9dccb16fc2'
down_revision = '217f272b9c26'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        CREATE TABLE qwc_config.permalinks (
            data text,
            key char(10),
            date date,
            PRIMARY KEY(key)
        );
    """)

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DROP TABLE qwc_config.permalinks;
    """)

    conn = op.get_bind()
    conn.execute(sql)
