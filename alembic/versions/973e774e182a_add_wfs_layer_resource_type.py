"""Add WFS Layer resource types

Revision ID: 973e774e182a
Revises: f59f5c7f2afa
Create Date: 2025-08-04 11:21:22.826534

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = '973e774e182a'
down_revision = 'f59f5c7f2afa'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        INSERT INTO {schema}.resource_types (name, description, list_order)
          VALUES (
            'wfs_service', 'WFS Service',
            (SELECT MAX(list_order) + 1 FROM {schema}.resource_types)
          );
        INSERT INTO {schema}.resource_types (name, description, list_order)
          VALUES (
            'wfs_layer', 'WFS Layer',
            (SELECT MAX(list_order) + 1 FROM {schema}.resource_types)
          );
        INSERT INTO {schema}.resource_types (name, description, list_order)
          VALUES (
            'wfs_layer_create', 'WFS Layer (create)',
            (SELECT MAX(list_order) + 1 FROM {schema}.resource_types)
          );
        INSERT INTO {schema}.resource_types (name, description, list_order)
          VALUES (
            'wfs_layer_update', 'WFS Layer (update)',
            (SELECT MAX(list_order) + 1 FROM {schema}.resource_types)
          );
        INSERT INTO {schema}.resource_types (name, description, list_order)
          VALUES (
            'wfs_layer_delete', 'WFS Layer (delete)',
            (SELECT MAX(list_order) + 1 FROM {schema}.resource_types)
          );
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DELETE FROM {schema}.resource_types WHERE name = 'wfs_service';
        DELETE FROM {schema}.resource_types WHERE name = 'wfs_layer';
        DELETE FROM {schema}.resource_types WHERE name = 'wfs_layer_create';
        DELETE FROM {schema}.resource_types WHERE name = 'wfs_layer_update';
        DELETE FROM {schema}.resource_types WHERE name = 'wfs_layer_delete';
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
