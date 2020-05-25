"""create table

Revision ID: 8f7167c09cba
Revises: 
Create Date: 2020-05-25 09:05:08.006790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f7167c09cba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "jornal_url",
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('jornal_name', sa.String, nullable=False),
        sa.Column('description', sa.String, nullable=False),
        sa.Column('image_url', sa.String, nullable=False),
        sa.Column('date_tsmp', sa.DateTime, nullable=False),
        sa.Column('date_str', sa.String, nullable=False),
        sa.Column('created', sa.DateTime, nullable=False),
    )


def downgrade():
    op.drop_table('jornal_url')
