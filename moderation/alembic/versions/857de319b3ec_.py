"""empty message

Revision ID: 857de319b3ec
Revises: 
Create Date: 2021-06-13 16:15:30.299559

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '857de319b3ec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('legalentitycreatorverificationrequest',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_uuid', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('moderated_at', sa.DateTime(), nullable=True),
    sa.Column('commentary', sa.String(), nullable=True),
    sa.Column('moderation_status', sa.Enum('in_progress', 'verified', 'declined', name='moderationstatus'), nullable=True),
    sa.Column('registration_certificate', sa.String(), nullable=False),
    sa.Column('executive_passport', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('executive_passport'),
    sa.UniqueConstraint('registration_certificate')
    )
    op.create_index(op.f('ix_legalentitycreatorverificationrequest_email'), 'legalentitycreatorverificationrequest', ['email'], unique=True)
    op.create_index(op.f('ix_legalentitycreatorverificationrequest_first_name'), 'legalentitycreatorverificationrequest', ['first_name'], unique=False)
    op.create_index(op.f('ix_legalentitycreatorverificationrequest_id'), 'legalentitycreatorverificationrequest', ['id'], unique=False)
    op.create_index(op.f('ix_legalentitycreatorverificationrequest_last_name'), 'legalentitycreatorverificationrequest', ['last_name'], unique=False)
    op.create_index(op.f('ix_legalentitycreatorverificationrequest_phone'), 'legalentitycreatorverificationrequest', ['phone'], unique=True)
    op.create_table('naturalpersoncreatorverificationrequest',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_uuid', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('moderated_at', sa.DateTime(), nullable=True),
    sa.Column('commentary', sa.String(), nullable=True),
    sa.Column('moderation_status', sa.Enum('in_progress', 'verified', 'declined', name='moderationstatus'), nullable=True),
    sa.Column('selfie_with_passport', sa.String(), nullable=False),
    sa.Column('passport', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('passport'),
    sa.UniqueConstraint('selfie_with_passport')
    )
    op.create_index(op.f('ix_naturalpersoncreatorverificationrequest_email'), 'naturalpersoncreatorverificationrequest', ['email'], unique=True)
    op.create_index(op.f('ix_naturalpersoncreatorverificationrequest_first_name'), 'naturalpersoncreatorverificationrequest', ['first_name'], unique=False)
    op.create_index(op.f('ix_naturalpersoncreatorverificationrequest_id'), 'naturalpersoncreatorverificationrequest', ['id'], unique=False)
    op.create_index(op.f('ix_naturalpersoncreatorverificationrequest_last_name'), 'naturalpersoncreatorverificationrequest', ['last_name'], unique=False)
    op.create_index(op.f('ix_naturalpersoncreatorverificationrequest_phone'), 'naturalpersoncreatorverificationrequest', ['phone'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_naturalpersoncreatorverificationrequest_phone'), table_name='naturalpersoncreatorverificationrequest')
    op.drop_index(op.f('ix_naturalpersoncreatorverificationrequest_last_name'), table_name='naturalpersoncreatorverificationrequest')
    op.drop_index(op.f('ix_naturalpersoncreatorverificationrequest_id'), table_name='naturalpersoncreatorverificationrequest')
    op.drop_index(op.f('ix_naturalpersoncreatorverificationrequest_first_name'), table_name='naturalpersoncreatorverificationrequest')
    op.drop_index(op.f('ix_naturalpersoncreatorverificationrequest_email'), table_name='naturalpersoncreatorverificationrequest')
    op.drop_table('naturalpersoncreatorverificationrequest')
    op.drop_index(op.f('ix_legalentitycreatorverificationrequest_phone'), table_name='legalentitycreatorverificationrequest')
    op.drop_index(op.f('ix_legalentitycreatorverificationrequest_last_name'), table_name='legalentitycreatorverificationrequest')
    op.drop_index(op.f('ix_legalentitycreatorverificationrequest_id'), table_name='legalentitycreatorverificationrequest')
    op.drop_index(op.f('ix_legalentitycreatorverificationrequest_first_name'), table_name='legalentitycreatorverificationrequest')
    op.drop_index(op.f('ix_legalentitycreatorverificationrequest_email'), table_name='legalentitycreatorverificationrequest')
    op.drop_table('legalentitycreatorverificationrequest')
    # ### end Alembic commands ###
