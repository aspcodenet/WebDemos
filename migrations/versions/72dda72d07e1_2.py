"""2.

Revision ID: 72dda72d07e1
Revises: 093dbfc20607
Create Date: 2021-12-30 14:40:01.682524

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72dda72d07e1'
down_revision = '093dbfc20607'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Accounts', sa.Column('CustomerId', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'Accounts', 'Customers', ['CustomerId'], ['Id'])
    op.add_column('Transactions', sa.Column('AccountId', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'Transactions', 'Accounts', ['AccountId'], ['Id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Transactions', type_='foreignkey')
    op.drop_column('Transactions', 'AccountId')
    op.drop_constraint(None, 'Accounts', type_='foreignkey')
    op.drop_column('Accounts', 'CustomerId')
    # ### end Alembic commands ###