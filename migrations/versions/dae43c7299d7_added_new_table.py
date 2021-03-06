"""added new table

Revision ID: dae43c7299d7
Revises: acaf1083c23f
Create Date: 2022-03-06 00:09:23.352083

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'dae43c7299d7'
down_revision = 'acaf1083c23f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('spreadsheet_version',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('version', sa.String(length=255), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_spreadsheet_version_id'), 'spreadsheet_version', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_spreadsheet_version_id'), table_name='spreadsheet_version')
    op.drop_table('spreadsheet_version')
    # ### end Alembic commands ###
