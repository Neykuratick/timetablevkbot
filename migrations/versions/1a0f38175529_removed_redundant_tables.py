"""removed redundant tables

Revision ID: 1a0f38175529
Revises: 5cc9083db9b7
Create Date: 2022-03-12 09:56:22.228791

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1a0f38175529'
down_revision = '5cc9083db9b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'users',
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('uuid', postgresql.UUID(), nullable=False),
        sa.Column('vk_id', sa.String(length=255), nullable=True),
        sa.Column('group_index', sa.Integer(), nullable=True),
        sa.Column('ai_companion_enabled', sa.Boolean(), nullable=True),
        sa.Column('last_activity', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('uuid')
    )
    op.create_index(op.f('ix_users_uuid'), 'users', ['uuid'], unique=False)
    op.create_table(
        'messages',
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_uuid', postgresql.UUID(), nullable=True),
        sa.Column('message_type', sa.Enum('READ', 'UPDATE', 'UNDEFINED', name='messagetype'),
                  nullable=True),
        sa.Column('message_intent',
                  sa.Enum('MONDAY_BELOW', 'MONDAY_ABOVE', 'TUESDAY_BELOW', 'TUESDAY_ABOVE',
                          'WEDNESDAY_BELOW', 'WEDNESDAY_ABOVE', 'THURSDAY_BELOW', 'THURSDAY_ABOVE',
                          'FRIDAY_BELOW', 'FRIDAY_ABOVE', 'SATURDAY_BELOW', 'SATURDAY_ABOVE', 'SETTINGS',
                          'GROUP', 'COMPANION', 'UPTIME', 'UNDEFINED', name='messageintent'),
                  nullable=True),
        sa.ForeignKeyConstraint(['user_uuid'], ['users.uuid'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_messages_id'), 'messages', ['id'], unique=False)
    op.drop_index('ix_google_credentials_id', table_name='google_credentials')
    op.drop_table('google_credentials')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'google_credentials',
        sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('service_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
        sa.Column('credentials', sa.VARCHAR(length=1000), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint('id', name='google_credentials_pkey'),
        sa.UniqueConstraint('credentials', name='google_credentials_credentials_key'),
        sa.UniqueConstraint('service_name', name='google_credentials_service_name_key')
    )
    op.create_index('ix_google_credentials_id', 'google_credentials', ['id'], unique=False)
    op.drop_index(op.f('ix_messages_id'), table_name='messages')
    op.drop_table('messages')
    op.drop_index(op.f('ix_users_uuid'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
