"""add data to resource_type

Revision ID: 217f272b9c26
Revises: db5a31995054
Create Date: 2018-07-24 11:10:35.963663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '217f272b9c26'
down_revision = 'db5a31995054'
branch_labels = None
depends_on = None


def upgrade():
    # NOTE: recreate resource_type, as the following does not work inside
    #       a transaction:
    #
    #         ALTER TYPE qwc_config.resource_type
    #           ADD VALUE 'data' AFTER 'attribute';
    sql = sa.sql.text("""
        ALTER TYPE qwc_config.resource_type
          RENAME TO resource_type_old;

        CREATE TYPE qwc_config.resource_type AS
          ENUM ('map', 'layer', 'attribute', 'data');

        ALTER TABLE qwc_config.resources
          ALTER COLUMN type TYPE qwc_config.resource_type
          USING type::text::qwc_config.resource_type;

        DROP TYPE qwc_config.resource_type_old;
    """)

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    # NOTE: removes resources of type 'data'
    sql = sa.sql.text("""
        DELETE FROM qwc_config.resources WHERE type = 'data';

        ALTER TYPE qwc_config.resource_type
          RENAME TO resource_type_old;

        CREATE TYPE qwc_config.resource_type AS
          ENUM ('map', 'layer', 'attribute');

        ALTER TABLE qwc_config.resources
          ALTER COLUMN type TYPE qwc_config.resource_type
          USING type::text::qwc_config.resource_type;

        DROP TYPE qwc_config.resource_type_old;
    """)

    conn = op.get_bind()
    conn.execute(sql)
