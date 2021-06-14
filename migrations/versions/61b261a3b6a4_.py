"""empty message

Revision ID: 61b261a3b6a4
Revises: f7c1c4137090
Create Date: 2021-06-13 07:51:46.140098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61b261a3b6a4'
down_revision = 'f7c1c4137090'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('completed_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    # ### end Alembic commands ###
