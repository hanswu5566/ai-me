"""empty message

Revision ID: e76ee3422ebc
Revises: 
Create Date: 2024-06-20 17:17:20.037073

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e76ee3422ebc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teammates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slack_user_id', sa.String(length=80), nullable=False),
    sa.Column('ios_teammates', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('web_teammates', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('android_teammates', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('backend_teammates', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('product_manager_teammates', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('product_designer_teammates', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slack_user_id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slack_user_id', sa.String(length=80), nullable=False),
    sa.Column('slack_team_id', sa.String(length=80), nullable=False),
    sa.Column('slack_user_name', sa.String(length=120), nullable=False),
    sa.Column('clickup_token', sa.String(length=120), nullable=True),
    sa.Column('clickup_user_id', sa.String(length=80), nullable=True),
    sa.Column('clickup_user_name', sa.String(length=120), nullable=True),
    sa.Column('clickup_team_id', sa.String(length=120), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('clickup_team_id'),
    sa.UniqueConstraint('clickup_token'),
    sa.UniqueConstraint('clickup_user_id'),
    sa.UniqueConstraint('slack_team_id'),
    sa.UniqueConstraint('slack_user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('teammates')
    # ### end Alembic commands ###
