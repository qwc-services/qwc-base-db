"""Rename Solr search facet resource

Revision ID: b24d92b5017f
Revises: 0307976d3d52
Create Date: 2024-08-08 10:49:29.172916

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = 'b24d92b5017f'
down_revision = '0307976d3d52'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        UPDATE {schema}.resource_types
        SET description = 'Search facet'
        WHERE name = 'solr_facet';
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        UPDATE {schema}.resource_types
        SET description = 'Solr search facet'
        WHERE name = 'solr_facet';
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
