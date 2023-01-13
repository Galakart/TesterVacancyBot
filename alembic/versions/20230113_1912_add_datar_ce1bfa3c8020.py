"""add datar

Revision ID: ce1bfa3c8020
Revises: a79d890524c3
Create Date: 2023-01-13 19:12:26.961084

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = 'ce1bfa3c8020'
down_revision = 'a79d890524c3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column('datar', sa.Date(), nullable=True))

    op.execute('UPDATE users SET datar="1990-04-15" WHERE id=111')
    op.execute('UPDATE users SET datar="1995-07-29" WHERE id=333')


def downgrade() -> None:
    op.drop_column('users', 'datar')
