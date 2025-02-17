"""empty message

Revision ID: 280199db43d2
Revises: e236c53e082a
Create Date: 2021-06-14 12:57:46.784498

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '280199db43d2'
down_revision = 'e236c53e082a'
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
