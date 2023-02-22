"""Initial migration

Revision ID: c402a605c41c
Revises: 03263795d3e1
Create Date: 2023-02-20 11:01:04.959876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c402a605c41c'
down_revision = '03263795d3e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('announcements', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(length=500), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('announcements', schema=None) as batch_op:
        batch_op.drop_column('title')

    # ### end Alembic commands ###