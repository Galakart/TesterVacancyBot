"""add category

Revision ID: f8562b3dc49d
Revises: a79d890524c3
Create Date: 2023-01-13 19:07:34.141558

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = 'f8562b3dc49d'
down_revision = 'a79d890524c3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column('category', sa.Integer(), nullable=True))

    op.execute('UPDATE users SET category=2 WHERE id=111')
    op.execute('UPDATE users SET category=1 WHERE id=222')
    op.execute('UPDATE users SET category=3 WHERE id=333')


def downgrade() -> None:
    op.drop_column('users', 'category')
