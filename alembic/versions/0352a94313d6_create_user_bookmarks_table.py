"""create user bookmarks table

Revision ID: 0352a94313d6
Revises: c77774920e5b
Create Date: 2021-04-15 14:58:38.844986

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0352a94313d6'
down_revision = 'c77774920e5b'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        CREATE TABLE qwc_config.user_bookmarks (
            username character varying NOT NULL,
            data text,
            key varchar(10),
            date date,
            description text,
            PRIMARY KEY(username, key)
        );
    """)

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DROP TABLE qwc_config.user_bookmarks;
    """)

    conn = op.get_bind()
    conn.execute(sql)
