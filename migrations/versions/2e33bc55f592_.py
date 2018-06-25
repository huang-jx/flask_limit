"""empty message

Revision ID: 2e33bc55f592
Revises: 
Create Date: 2018-06-21 13:09:36.904571

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e33bc55f592'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cate',
    sa.Column('cid', sa.Integer(), nullable=False),
    sa.Column('cname', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('cid')
    )
    op.create_index(op.f('ix_cate_cname'), 'cate', ['cname'], unique=True)
    op.create_table('user',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('weight', sa.Float(precision=10, asdecimal=2), nullable=True),
    sa.Column('money', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('msg', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_index(op.f('ix_user_name'), 'user', ['name'], unique=True)
    op.create_table('shop',
    sa.Column('sid', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('cid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cid'], ['cate.cid'], ),
    sa.PrimaryKeyConstraint('sid')
    )
    op.create_index(op.f('ix_shop_name'), 'shop', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_shop_name'), table_name='shop')
    op.drop_table('shop')
    op.drop_index(op.f('ix_user_name'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_cate_cname'), table_name='cate')
    op.drop_table('cate')
    # ### end Alembic commands ###