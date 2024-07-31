"""Create last_update

Revision ID: db5a31995054
Revises: 56846d9f2753
Create Date: 2018-07-06 15:54:58.460134

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = 'db5a31995054'
down_revision = '56846d9f2753'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        CREATE TABLE {schema}.last_update (
          updated_at timestamp without time zone NOT NULL,
          CONSTRAINT last_update_pk PRIMARY KEY (updated_at)
        );
        INSERT INTO {schema}.last_update (updated_at)
          VALUES(current_timestamp);
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DROP TABLE {schema}.last_update;
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
