"""empty message

Revision ID: 31d5b6ce5125
Revises: b8be05558079
Create Date: 2019-02-11 11:51:39.395897

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31d5b6ce5125'
down_revision = 'b8be05558079'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('bake_wash', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order', 'bake_wash')
    # ### end Alembic commands ###
