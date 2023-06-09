"""orders table

Revision ID: fb4419cb6071
Revises: cef4951ef870
Create Date: 2023-03-29 11:05:16.760151

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb4419cb6071'
down_revision = 'cef4951ef870'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ordered_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('total_price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('add_drinks', sa.Column('order_number', sa.Integer(), nullable=True))
    op.add_column('add_drinks', sa.Column('size_price', sa.Integer(), nullable=True))
    op.drop_constraint(None, 'add_drinks', type_='foreignkey')
    op.create_foreign_key(None, 'add_drinks', 'orders', ['order_number'], ['id'])
    op.create_foreign_key(None, 'add_drinks', 'drinks', ['drink_name'], ['name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'add_drinks', type_='foreignkey')
    op.drop_constraint(None, 'add_drinks', type_='foreignkey')
    op.create_foreign_key(None, 'add_drinks', 'drinks', ['drink_name'], ['id'])
    op.drop_column('add_drinks', 'size_price')
    op.drop_column('add_drinks', 'order_number')
    op.drop_table('orders')
    # ### end Alembic commands ###
