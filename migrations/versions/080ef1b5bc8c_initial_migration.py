"""Initial Migration

Revision ID: 080ef1b5bc8c
Revises: b9d23b7deaa0
Create Date: 2020-04-13 21:08:11.324017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '080ef1b5bc8c'
down_revision = 'b9d23b7deaa0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=255), nullable=True))
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    op.drop_column('users', 'pass_secure')
    op.drop_column('users', 'password_harsh')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_harsh', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('pass_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###