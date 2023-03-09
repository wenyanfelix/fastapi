"""add foreign-key to posts table

Revision ID: 74901b33bf3c
Revises: db835879be1f
Create Date: 2023-03-09 23:08:36.467253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74901b33bf3c'
down_revision = 'db835879be1f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
