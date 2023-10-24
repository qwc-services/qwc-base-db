"""Create resources and permissions

Revision ID: b21139053154
Revises: 9c671585cfb1
Create Date: 2018-07-03 13:09:23.087429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b21139053154'
down_revision = '9c671585cfb1'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        CREATE TYPE qwc_config.resource_type AS
          ENUM ('map', 'layer', 'attribute');

        CREATE TABLE qwc_config.resources (
          id serial NOT NULL,
          parent_id integer,
          type qwc_config.resource_type NOT NULL,
          name character varying NOT NULL,
          CONSTRAINT resources_pk PRIMARY KEY (id),
          CONSTRAINT parent_fk FOREIGN KEY (parent_id)
              REFERENCES qwc_config.resources (id) MATCH FULL
              ON UPDATE CASCADE ON DELETE RESTRICT
        );

        CREATE TABLE qwc_config.permissions (
          id serial NOT NULL,
          role_id integer NOT NULL,
          resource_id integer NOT NULL,
          priority integer NOT NULL DEFAULT 0,
          write boolean NOT NULL DEFAULT FALSE,
          CONSTRAINT permissions_pk PRIMARY KEY (id),
          CONSTRAINT role_fk FOREIGN KEY (role_id)
              REFERENCES qwc_config.roles (id) MATCH FULL
              ON UPDATE CASCADE ON DELETE RESTRICT,
          CONSTRAINT resource_fk FOREIGN KEY (resource_id)
              REFERENCES qwc_config.resources (id) MATCH FULL
              ON UPDATE CASCADE ON DELETE RESTRICT
        );
    """)

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DROP TABLE qwc_config.resources CASCADE;
        DROP TABLE qwc_config.permissions CASCADE;
        DROP TYPE qwc_config.resource_type;
    """)

    conn = op.get_bind()
    conn.execute(sql)
