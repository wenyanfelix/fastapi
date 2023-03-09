"""add columns to posts

Revision ID: 629aa8d88dcd
Revises: 74901b33bf3c
Create Date: 2023-03-09 23:16:00.075568

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '629aa8d88dcd'
down_revision = '74901b33bf3c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',
                  sa.Column('published', sa.Boolean(),
                            nullable=False, server_default='TRUE'),)
    op.add_column('posts',
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                            nullable=False, server_default=sa.text('NOW()')),)


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
