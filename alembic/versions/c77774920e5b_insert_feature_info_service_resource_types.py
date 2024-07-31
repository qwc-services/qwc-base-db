"""Insert feature info service resource types

Revision ID: c77774920e5b
Revises: 9168093625bd
Create Date: 2020-08-13 11:11:03.020251

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = 'c77774920e5b'
down_revision = '9168093625bd'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        INSERT INTO {schema}.resource_types (name, description, list_order)
          VALUES (
            'feature_info_service', 'FeatureInfo service',
            (SELECT MAX(list_order) + 1 FROM {schema}.resource_types)
          );
        INSERT INTO {schema}.resource_types (name, description, list_order)
          VALUES (
            'feature_info_layer', 'FeatureInfo layer',
            (SELECT MAX(list_order) + 1 FROM {schema}.resource_types)
          );
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DELETE FROM {schema}.resource_types
          WHERE name = 'feature_info_service';
        DELETE FROM {schema}.resource_types
          WHERE name = 'feature_info_layer';
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
