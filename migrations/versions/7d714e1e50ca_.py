"""empty message

Revision ID: 7d714e1e50ca
Revises: 
Create Date: 2023-04-09 17:00:34.896154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d714e1e50ca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(length=150), nullable=False),
    sa.Column('last_name', sa.String(length=150), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('g_auth_verify', sa.Boolean(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('book',
    sa.Column('isbn', sa.String(length=15), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.Column('author', sa.String(length=150), nullable=False),
    sa.Column('length', sa.Integer(), nullable=True),
    sa.Column('cover', sa.String(length=150), nullable=True),
    sa.Column('copyright', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(length=2500), nullable=True),
    sa.Column('user_id', sa.String(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('isbn')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    op.drop_table('user')
    # ### end Alembic commands ###