"""create posts table

Revision ID: 4217b11d5d83
Revises: 
Create Date: 2022-01-13 23:40:14.752161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4217b11d5d83'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(),
                    nullable=False, primary_key=True), )


def downgrade():
    op.drop_table('posts')
