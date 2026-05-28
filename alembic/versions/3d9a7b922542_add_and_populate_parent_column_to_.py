"""Add and populate parent column to resource_types

Revision ID: 3d9a7b922542
Revises: 417fb25a35fd
Create Date: 2026-05-28 10:40:33.819481

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = '3d9a7b922542'
down_revision = '417fb25a35fd'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        ALTER TABLE {schema}.resource_types
          ADD COLUMN parents character varying[] DEFAULT '{{}}';
        ALTER TABLE {schema}.resource_types
          ADD COLUMN parent_is_default_allow boolean DEFAULT FALSE;

        UPDATE {schema}.resource_types SET parents = ARRAY['map'] WHERE name = 'layer';
        UPDATE {schema}.resource_types SET parents = ARRAY['layer', 'data', 'wfs_layer', 'feature_info_layer'] WHERE name = 'attribute';
        UPDATE {schema}.resource_types SET parents = ARRAY['map'] WHERE name = 'print_template';
        UPDATE {schema}.resource_types SET parents = ARRAY['map'] WHERE name = 'data';
        UPDATE {schema}.resource_types SET parents = ARRAY['map'] WHERE name = 'data_create';
        UPDATE {schema}.resource_types SET parents = ARRAY['map'] WHERE name = 'data_update';
        UPDATE {schema}.resource_types SET parents = ARRAY['map'] WHERE name = 'data_delete';
        UPDATE {schema}.resource_types SET parents = ARRAY['wfs_service'] WHERE name = 'wfs_layer';
        UPDATE {schema}.resource_types SET parents = ARRAY['wfs_service'] WHERE name = 'wfs_layer_create';
        UPDATE {schema}.resource_types SET parents = ARRAY['wfs_service'] WHERE name = 'wfs_layer_update';
        UPDATE {schema}.resource_types SET parents = ARRAY['wfs_service'] WHERE name = 'wfs_layer_delete';
        UPDATE {schema}.resource_types SET parents = ARRAY['map'] WHERE name = 'object3d';
        UPDATE {schema}.resource_types SET parents = ARRAY['plugin'] WHERE name = 'plugin_data';
        UPDATE {schema}.resource_types SET parents = ARRAY['feature_info_service'] WHERE name = 'feature_info_layer';

        UPDATE {schema}.resource_types SET parent_is_default_allow = TRUE WHERE name = 'attribute';
        UPDATE {schema}.resource_types SET parent_is_default_allow = TRUE WHERE name = 'layer';
        UPDATE {schema}.resource_types SET parent_is_default_allow = TRUE WHERE name = 'feature_info_layer';
        UPDATE {schema}.resource_types SET parent_is_default_allow = TRUE WHERE name = 'print_template';
        UPDATE {schema}.resource_types SET parent_is_default_allow = TRUE WHERE name = 'object3d';
        UPDATE {schema}.resource_types SET parent_is_default_allow = TRUE WHERE name = 'data';
        UPDATE {schema}.resource_types SET parent_is_default_allow = TRUE WHERE name = 'data_create';
        UPDATE {schema}.resource_types SET parent_is_default_allow = TRUE WHERE name = 'data_update';
        UPDATE {schema}.resource_types SET parent_is_default_allow = TRUE WHERE name = 'data_delete';
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        ALTER TABLE {schema}.resource_types DROP COLUMN parents;
        ALTER TABLE {schema}.resource_types DROP COLUMN parent_is_default_allow;
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
