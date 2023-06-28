"""empty message

Revision ID: 6a481a5a6bb4
Revises: a95f5ee8ef0e
Create Date: 2023-06-26 22:01:20.458285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a481a5a6bb4'
down_revision = 'a95f5ee8ef0e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('isDisabled', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('isDisabled')

    # ### end Alembic commands ###
