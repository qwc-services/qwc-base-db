"""Add oblique_image_dataset resource type

Revision ID: 6e095634bbeb
Revises: 6a51097570a0
Create Date: 2026-01-05 14:24:53.772487

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = '6e095634bbeb'
down_revision = '6a51097570a0'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        INSERT INTO {schema}.resource_types (name, description, list_order)
          VALUES (
            'oblique_image_dataset', 'Oblique Image Dataset',
            (SELECT MAX(list_order) + 1 FROM {schema}.resource_types)
          );
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DELETE FROM {schema}.resource_types WHERE name = 'oblique_image_dataset';
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
