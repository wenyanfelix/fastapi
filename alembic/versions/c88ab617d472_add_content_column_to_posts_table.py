"""add content column to posts table

Revision ID: c88ab617d472
Revises: eef86b311ed2
Create Date: 2023-03-09 00:05:19.257294

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c88ab617d472'
down_revision = 'eef86b311ed2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
