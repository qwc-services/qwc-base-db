"""Create user_visibility_presets table

Revision ID: 6a51097570a0
Revises: 4aa92e9eb2c0
Create Date: 2025-12-24 16:10:44.071241

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = '6a51097570a0'
down_revision = '4aa92e9eb2c0'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        CREATE TABLE {schema}.user_visibility_presets (
            username character varying NOT NULL,
            data text,
            key varchar(10),
            date date,
            description text,
            PRIMARY KEY(username, key)
        );
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DROP TABLE {schema}.user_visibility_presets;
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
