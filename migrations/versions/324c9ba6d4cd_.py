"""empty message

Revision ID: 324c9ba6d4cd
Revises: a857cba33efd
Create Date: 2021-06-14 12:13:45.923074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '324c9ba6d4cd'
down_revision = 'a857cba33efd'
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
