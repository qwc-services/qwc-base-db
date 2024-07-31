"""Insert public role

Revision ID: f805e8e4a791
Revises: b21139053154
Create Date: 2018-07-03 13:11:00.253559

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = 'f805e8e4a791'
down_revision = 'b21139053154'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        INSERT INTO {schema}.roles (name, description)
          VALUES ('public', 'Public role');
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DELETE FROM {schema}.roles WHERE name = 'public';
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
