"""Insert solr_facet resource type

Revision ID: 9168093625bd
Revises: 0fa6610ee212
Create Date: 2020-08-13 11:08:43.109973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9168093625bd'
down_revision = '0fa6610ee212'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        INSERT INTO qwc_config.resource_types (name, description, list_order)
          VALUES (
            'solr_facet', 'Solr search facet',
            (SELECT MAX(list_order) + 1 FROM qwc_config.resource_types)
          );
    """)

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DELETE FROM qwc_config.resource_types WHERE name = 'solr_facet';
    """)

    conn = op.get_bind()
    conn.execute(sql)
