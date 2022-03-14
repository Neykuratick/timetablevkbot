"""updated type string to text in class

Revision ID: 5f2e53bab951
Revises: 4900652dabea
Create Date: 2022-03-11 02:52:31.989191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f2e53bab951'
down_revision = '4900652dabea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('classes', 'text')
    op.add_column('classes', sa.Column('text', sa.UnicodeText(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('classes', 'text')
    op.add_column('classes', sa.Column('text', sa.String(length=1000), nullable=True))
    # ### end Alembic commands ###
