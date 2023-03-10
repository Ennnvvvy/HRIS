"""empty message

Revision ID: 6ba4e1f913f2
Revises: 1445d655c7d1
Create Date: 2023-02-22 14:18:02.237501

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ba4e1f913f2'
down_revision = '1445d655c7d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('salaries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('salary_name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('per_hour', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('employee_info', schema=None) as batch_op:
        batch_op.add_column(sa.Column('salary_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'salaries', ['salary_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employee_info', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('salary_id')

    op.drop_table('salaries')
    # ### end Alembic commands ###
