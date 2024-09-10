"""Add document_templates resource type

Revision ID: 66d912f96db6
Revises: b24d92b5017f
Create Date: 2024-09-10 16:07:01.068732

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = '66d912f96db6'
down_revision = 'b24d92b5017f'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        INSERT INTO {schema}.resource_types(name, description, list_order)
        VALUES ('document_templates', 'Document template', 18);
    """.format(schema=qwc_config_schema))
    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DELETE FROM {schema}.resource_types
        WHERE name = 'document_templates';
    """.format(schema=qwc_config_schema))
    conn = op.get_bind()
    conn.execute(sql)
