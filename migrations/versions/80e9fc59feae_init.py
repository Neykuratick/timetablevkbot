"""init

Revision ID: 80e9fc59feae
Revises: 
Create Date: 2022-03-05 14:22:26.025398

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '80e9fc59feae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'classes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('absolute_index', sa.Integer(), nullable=True),
        sa.Column('group_id', sa.Integer(), nullable=True),
        sa.Column('text', sa.String(length=255), nullable=True),
        sa.Column('links', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('absolute_index')
    )
    op.create_index(op.f('ix_classes_id'), 'classes', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_classes_id'), table_name='classes')
    op.drop_table('classes')
    # ### end Alembic commands ###
