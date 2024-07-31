"""Insert solr_facet resource type

Revision ID: 9168093625bd
Revises: 0fa6610ee212
Create Date: 2020-08-13 11:08:43.109973

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = '9168093625bd'
down_revision = '0fa6610ee212'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        INSERT INTO {schema}.resource_types (name, description, list_order)
          VALUES (
            'solr_facet', 'Solr search facet',
            (SELECT MAX(list_order) + 1 FROM {schema}.resource_types)
          );
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DELETE FROM {schema}.resource_types WHERE name = 'solr_facet';
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
