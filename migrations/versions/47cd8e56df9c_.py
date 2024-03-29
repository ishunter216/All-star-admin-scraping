"""empty message

Revision ID: 47cd8e56df9c
Revises: b613524661fa
Create Date: 2018-05-08 11:48:05.187116

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47cd8e56df9c'
down_revision = 'b613524661fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('approval_comments', sa.String(length=128), nullable=True))
    op.add_column('order', sa.Column('approval_employee_code', sa.String(length=32), nullable=True))
    op.add_column('order', sa.Column('correct_to_invoice', sa.Boolean(), nullable=True))
    op.add_column('order', sa.Column('have_repair', sa.Boolean(), nullable=True))
    op.add_column('order', sa.Column('induction_employee_code', sa.String(length=32), nullable=True))
    op.add_column('order', sa.Column('light_approved', sa.String(length=10), nullable=True))
    op.add_column('order', sa.Column('notes', sa.String(length=128), nullable=True))
    op.add_column('order', sa.Column('po_light', sa.Boolean(), nullable=True))
    op.add_column('order', sa.Column('repair_comments', sa.String(length=128), nullable=True))
    op.add_column('order', sa.Column('replacement_available', sa.Boolean(), nullable=True))
    op.add_column('order', sa.Column('replacement_comments', sa.String(length=128), nullable=True))
    op.add_column('order', sa.Column('side', sa.String(length=32), nullable=True))
    op.add_column('order', sa.Column('status', sa.String(length=64), nullable=True))
    op.add_column('order', sa.Column('stickered_engraved', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order', 'stickered_engraved')
    op.drop_column('order', 'status')
    op.drop_column('order', 'side')
    op.drop_column('order', 'replacement_comments')
    op.drop_column('order', 'replacement_available')
    op.drop_column('order', 'repair_comments')
    op.drop_column('order', 'po_light')
    op.drop_column('order', 'notes')
    op.drop_column('order', 'light_approved')
    op.drop_column('order', 'induction_employee_code')
    op.drop_column('order', 'have_repair')
    op.drop_column('order', 'correct_to_invoice')
    op.drop_column('order', 'approval_employee_code')
    op.drop_column('order', 'approval_comments')
    # ### end Alembic commands ###
