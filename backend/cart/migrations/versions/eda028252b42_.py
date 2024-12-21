"""empty message

Revision ID: eda028252b42
Revises: 80dc15698d12
Create Date: 2024-12-01 19:26:31.115951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eda028252b42'
down_revision = '80dc15698d12'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(length=80), nullable=False),
    sa.Column('product_price', sa.Float(), nullable=False),
    sa.Column('product_quantity', sa.Integer(), nullable=False),
    sa.Column('product_image', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('product_image'),
    sa.UniqueConstraint('product_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cart')
    # ### end Alembic commands ###