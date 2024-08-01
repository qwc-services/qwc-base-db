"""Create user_infos

Add additional user fields in a separate qwc_config.table user_infos
with a one-to-one relation to qwc_config.users.

Revision ID: 0f409f15e0b7
Revises: b0cb86db3dfe
Create Date: 2018-12-17 10:59:38.886407

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = '0f409f15e0b7'
down_revision = 'b0cb86db3dfe'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        CREATE TABLE {schema}.user_infos (
          user_id integer NOT NULL,
          CONSTRAINT user_infos_pk PRIMARY KEY (user_id),
          CONSTRAINT user_fk FOREIGN KEY (user_id)
              REFERENCES {schema}.users (id) MATCH FULL
              ON UPDATE CASCADE ON DELETE RESTRICT
        );
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DROP TABLE {schema}.user_infos CASCADE;
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
