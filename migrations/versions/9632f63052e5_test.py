"""'test'

Revision ID: 9632f63052e5
Revises: fcc53b9552f2
Create Date: 2023-02-22 19:58:13.331040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9632f63052e5'
down_revision = 'fcc53b9552f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('positions', schema=None) as batch_op:
        batch_op.drop_constraint('positions_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'departments', ['department_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('positions', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('positions_ibfk_1', 'departments', ['department_id'], ['id'])

    # ### end Alembic commands ###
