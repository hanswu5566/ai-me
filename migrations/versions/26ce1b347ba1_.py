"""empty message

Revision ID: 26ce1b347ba1
Revises: 0929a66c1801
Create Date: 2024-06-12 09:02:23.114998

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26ce1b347ba1'
down_revision = '0929a66c1801'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('slack_user_name', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('clickup_user_name', sa.String(length=120), nullable=False))
        batch_op.drop_column('slack_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('slack_name', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.drop_column('clickup_user_name')
        batch_op.drop_column('slack_user_name')

    # ### end Alembic commands ###
