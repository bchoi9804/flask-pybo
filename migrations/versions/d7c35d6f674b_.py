"""empty message

Revision ID: d7c35d6f674b
Revises: baf4c18c4316
Create Date: 2022-04-07 12:06:53.958555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7c35d6f674b'
down_revision = 'baf4c18c4316'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_user_email'), ['email'])
        batch_op.create_unique_constraint(batch_op.f('uq_user_username'), ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_user_username'), type_='unique')
        batch_op.drop_constraint(batch_op.f('uq_user_email'), type_='unique')

    # ### end Alembic commands ###
