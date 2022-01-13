"""add columns to posts

Revision ID: 77e30fd9fb1a
Revises: 1f2a27beda7d
Create Date: 2022-01-14 01:42:05.209940

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '77e30fd9fb1a'
down_revision = '1f2a27beda7d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(),
                  nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text("now()")))
    pass


def downgrade():
    op.drop_column('posts', 'created_at')
    op.drop_column('posts', 'published')
    pass
