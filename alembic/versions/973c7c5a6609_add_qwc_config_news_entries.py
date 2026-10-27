"""Add qwc_config.news_entries

Revision ID: 973c7c5a6609
Revises: bb61518dc5ad
Create Date: 2026-10-27 08:19:55.384356

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = '973c7c5a6609'
down_revision = 'bb61518dc5ad'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        CREATE TABLE {schema}.news_entries (
            id serial PRIMARY KEY,
            body text,
            lang character varying,
            date date NOT NULL DEFAULT NOW()
        );
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DROP TABLE {schema}.news_entries;
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
