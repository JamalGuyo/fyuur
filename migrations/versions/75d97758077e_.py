"""empty message

Revision ID: 75d97758077e
Revises: 835261c6c970
Create Date: 2022-08-26 16:50:04.859026

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '75d97758077e'
down_revision = '835261c6c970'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Shows',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('Show')
    op.add_column('Artist', sa.Column('website', sa.String(length=120), nullable=True))
    op.alter_column('Artist', 'genres',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.drop_column('Artist', 'website_link')
    op.add_column('Venue', sa.Column('website', sa.String(length=120), nullable=True))
    op.alter_column('Venue', 'genres',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.drop_column('Venue', 'website_link')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('website_link', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.alter_column('Venue', 'genres',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.drop_column('Venue', 'website')
    op.add_column('Artist', sa.Column('website_link', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.alter_column('Artist', 'genres',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.drop_column('Artist', 'website')
    op.create_table('Show',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Show_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('start_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], name='Show_artist_id_fkey'),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], name='Show_venue_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='Show_pkey')
    )
    op.drop_table('Shows')
    # ### end Alembic commands ###
