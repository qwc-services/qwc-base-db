"""Insert more detailed data resource types for CRUD

Revision ID: a793057bbf20
Revises: 0f409f15e0b7
Create Date: 2018-12-18 16:12:42.010630

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = 'a793057bbf20'
down_revision = '0f409f15e0b7'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        INSERT INTO {schema}.resource_types (name, description, list_order)
          VALUES (
            'data_create', 'Data (create)',
            (SELECT MAX(list_order) + 1 FROM {schema}.resource_types)
          );
        INSERT INTO {schema}.resource_types (name, description, list_order)
          VALUES (
            'data_read', 'Data (read)',
            (SELECT MAX(list_order) + 1 FROM {schema}.resource_types)
          );
        INSERT INTO {schema}.resource_types (name, description, list_order)
          VALUES (
            'data_update', 'Data (update)',
            (SELECT MAX(list_order) + 1 FROM {schema}.resource_types)
          );
        INSERT INTO {schema}.resource_types (name, description, list_order)
          VALUES (
            'data_delete', 'Data (delete)',
            (SELECT MAX(list_order) + 1 FROM {schema}.resource_types)
          );
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DELETE FROM {schema}.resource_types WHERE name = 'data_create';
        DELETE FROM {schema}.resource_types WHERE name = 'data_read';
        DELETE FROM {schema}.resource_types WHERE name = 'data_update';
        DELETE FROM {schema}.resource_types WHERE name = 'data_delete';
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
