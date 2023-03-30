"""Hopefully fix the models with connection to DB

Revision ID: f26b11933ef7
Revises: fb4419cb6071
Create Date: 2023-03-29 15:28:01.686449

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f26b11933ef7'
down_revision = 'fb4419cb6071'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'add_drinks', type_='foreignkey')
    op.create_foreign_key(None, 'add_drinks', 'orders', ['order_number'], ['id'])
    op.create_foreign_key(None, 'add_drinks', 'drinks', ['drink_name'], ['name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'add_drinks', type_='foreignkey')
    op.drop_constraint(None, 'add_drinks', type_='foreignkey')
    op.create_foreign_key(None, 'add_drinks', 'drinks', ['drink_name'], ['id'])
    # ### end Alembic commands ###
