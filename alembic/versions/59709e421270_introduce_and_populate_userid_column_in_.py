"""Introduce and populate userid column in bookmarks table

Revision ID: 59709e421270
Revises: 66d912f96db6
Create Date: 2024-12-13 10:07:25.614981

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = '59709e421270'
down_revision = '66d912f96db6'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        ALTER TABLE {schema}.user_bookmarks
        ADD COLUMN user_id integer;
    """.format(schema=qwc_config_schema))
    conn = op.get_bind()
    conn.execute(sql)

    sql = sa.sql.text("""
        UPDATE {schema}.user_bookmarks
        SET user_id = users.id
        FROM {schema}.users
        WHERE user_bookmarks.username = users.name;
    """.format(schema=qwc_config_schema))
    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        ALTER TABLE {schema}.user_bookmarks
        DROP COLUMN user_id;
    """.format(schema=qwc_config_schema))
    conn = op.get_bind()
    conn.execute(sql)
