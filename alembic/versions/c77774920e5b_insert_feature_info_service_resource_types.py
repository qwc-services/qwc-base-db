"""Insert feature info service resource types

Revision ID: c77774920e5b
Revises: 9168093625bd
Create Date: 2020-08-13 11:11:03.020251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c77774920e5b'
down_revision = '9168093625bd'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        INSERT INTO qwc_config.resource_types (name, description, list_order)
          VALUES (
            'feature_info_service', 'FeatureInfo service',
            (SELECT MAX(list_order) + 1 FROM qwc_config.resource_types)
          );
        INSERT INTO qwc_config.resource_types (name, description, list_order)
          VALUES (
            'feature_info_layer', 'FeatureInfo layer',
            (SELECT MAX(list_order) + 1 FROM qwc_config.resource_types)
          );
    """)

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DELETE FROM qwc_config.resource_types
          WHERE name = 'feature_info_service';
        DELETE FROM qwc_config.resource_types
          WHERE name = 'feature_info_layer';
    """)

    conn = op.get_bind()
    conn.execute(sql)
