"""Initial migration.

Revision ID: 28e2eee93967
Revises: 
Create Date: 2021-08-15 13:30:26.810853

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28e2eee93967'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('meta_description', sa.String(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'meta_description')
    # ### end Alembic commands ###
