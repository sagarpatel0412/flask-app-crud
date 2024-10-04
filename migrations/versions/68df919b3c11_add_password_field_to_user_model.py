"""Add password field to User model

Revision ID: 68df919b3c11
Revises: 
Create Date: 2024-10-04 16:06:42.660185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68df919b3c11'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=128), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('password')

    # ### end Alembic commands ###
