"""add columns

Revision ID: 1bb28ba564a5
Revises: 4217b11d5d83
Create Date: 2022-01-14 01:17:24.659588

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1bb28ba564a5'
down_revision = '4217b11d5d83'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('title', sa.String(), nullable=False))


def downgrade():
    op.drop_column('posts', 'title')
