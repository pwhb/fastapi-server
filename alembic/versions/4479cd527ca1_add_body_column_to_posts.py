"""add body column to posts

Revision ID: 4479cd527ca1
Revises: 1bb28ba564a5
Create Date: 2022-01-14 01:23:49.383737

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4479cd527ca1'
down_revision = '1bb28ba564a5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('body', sa.String(), nullable=False),)

    pass


def downgrade():
    op.drop_column('posts', 'body')
    pass
