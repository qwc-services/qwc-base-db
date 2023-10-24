"""Create user_infos

Add additional user fields in a separate qwc_config.table user_infos
with a one-to-one relation to qwc_config.users.

Revision ID: 0f409f15e0b7
Revises: b0cb86db3dfe
Create Date: 2018-12-17 10:59:38.886407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f409f15e0b7'
down_revision = 'b0cb86db3dfe'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        CREATE TABLE qwc_config.user_infos (
          user_id integer NOT NULL,
          CONSTRAINT user_infos_pk PRIMARY KEY (user_id),
          CONSTRAINT user_fk FOREIGN KEY (user_id)
              REFERENCES qwc_config.users (id) MATCH FULL
              ON UPDATE CASCADE ON DELETE RESTRICT
        );
    """)

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DROP TABLE qwc_config.user_infos CASCADE;
    """)

    conn = op.get_bind()
    conn.execute(sql)
