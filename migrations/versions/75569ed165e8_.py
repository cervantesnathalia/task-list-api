"""empty message

Revision ID: 75569ed165e8
Revises: 63d7616a1ed1
Create Date: 2021-06-16 18:45:01.564949

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75569ed165e8'
down_revision = '63d7616a1ed1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('goal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('goal')
    # ### end Alembic commands ###
