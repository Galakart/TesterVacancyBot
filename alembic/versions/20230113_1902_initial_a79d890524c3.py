"""initial

Revision ID: a79d890524c3
Revises: 
Create Date: 2023-01-13 19:02:10.220532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a79d890524c3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('fio', sa.String(length=100), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    comment='Юзеры бота'
                    )

    op.execute('INSERT INTO users VALUES (111, "Иванов Иван")')
    op.execute('INSERT INTO users VALUES (222, "Сидоров Сидор")')
    op.execute('INSERT INTO users VALUES (333, "Тестов Тест")')


def downgrade() -> None:
    op.drop_table('users')
