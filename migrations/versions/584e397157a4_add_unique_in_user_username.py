"""add unique in user.username

Revision ID: 584e397157a4
Revises: 68df919b3c11
Create Date: 2024-10-04 16:16:49.139155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '584e397157a4'
down_revision = '68df919b3c11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
