"""add users table

Revision ID: d6a7fb59c873
Revises: 4479cd527ca1
Create Date: 2022-01-14 01:27:53.669869

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6a7fb59c873'
down_revision = '4479cd527ca1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')

                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
