"""actually REALLY built drinks

Revision ID: b1a8415326e3
Revises: 335e607e8076
Create Date: 2023-03-27 14:36:58.360071

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1a8415326e3'
down_revision = '335e607e8076'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('drinks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('hot', sa.Boolean(), nullable=True),
    sa.Column('size', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_drinks_name'), 'drinks', ['name'], unique=False)
    op.drop_index('ix_students_name', table_name='students')
    op.drop_table('students')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('email', sa.VARCHAR(length=55), nullable=True),
    sa.Column('grade', sa.INTEGER(), nullable=True),
    sa.Column('birthday', sa.DATETIME(), nullable=True),
    sa.Column('enrolled_date', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_students_name', 'students', ['name'], unique=False)
    op.drop_index(op.f('ix_drinks_name'), table_name='drinks')
    op.drop_table('drinks')
    # ### end Alembic commands ###
