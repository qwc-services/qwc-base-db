"""Create password_histories

Add password histories for tracking some optional password constraints
in QWC DB Auth Service.

NOTE: Foreign key constraint is set to automatically remove
related history entries on user delete

Revision ID: ad5e7b02469a
Revises: 0352a94313d6
Create Date: 2022-04-13 11:06:38.665469

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = 'ad5e7b02469a'
down_revision = '0352a94313d6'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        CREATE TABLE {schema}.password_histories (
          id serial NOT NULL,
          user_id integer NOT NULL,
          password_hash character varying(128),
          created_at timestamp without time zone NOT NULL,
          CONSTRAINT password_histories_pk PRIMARY KEY (id),
          CONSTRAINT user_fk FOREIGN KEY (user_id)
              REFERENCES {schema}.users (id) MATCH FULL
              ON UPDATE CASCADE ON DELETE CASCADE
        );
        COMMENT ON TABLE {schema}.password_histories IS
            'Password histories for tracking some optional password constraints in QWC DB Auth Service';
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DROP TABLE {schema}.password_histories CASCADE;
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
