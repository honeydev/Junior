"""empty message

Revision ID: 22cd0b59ef9c
Revises: 94cb730fe665
Create Date: 2019-10-10 15:48:24.958462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22cd0b59ef9c'
down_revision = '94cb730fe665'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answers', sa.Column('is_admin_answer', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('answers', 'is_admin_answer')
    # ### end Alembic commands ###
