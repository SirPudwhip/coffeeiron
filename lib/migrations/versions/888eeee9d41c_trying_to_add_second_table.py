"""trying to add second table

Revision ID: 888eeee9d41c
Revises: b1a8415326e3
Create Date: 2023-03-27 14:41:34.944392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '888eeee9d41c'
down_revision = 'b1a8415326e3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_customers_name'), 'customers', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_customers_name'), table_name='customers')
    op.drop_table('customers')
    # ### end Alembic commands ###
