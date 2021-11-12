"""Add beach_id column and BeachForecastListHistory table

Revision ID: eae746ee3547
Revises: cc49b6b03c5a
Create Date: 2021-11-06 03:37:19.196002

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'eae746ee3547'
down_revision = 'cc49b6b03c5a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('beachforecastlisthistory',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_dt', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('update_dt', postgresql.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('beach', sa.String(), nullable=True),
    sa.Column('region', sa.String(), nullable=True),
    sa.Column('ocean', sa.String(), nullable=True),
    sa.Column('beach_id', sa.Integer(), nullable=True),
    sa.Column('live_info', sa.JSON(), nullable=True),
    sa.Column('forecast_info', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_beachforecastlisthistory_beach'), 'beachforecastlisthistory', ['beach'], unique=False)
    op.create_index(op.f('ix_beachforecastlisthistory_beach_id'), 'beachforecastlisthistory', ['beach_id'], unique=False)
    op.create_index(op.f('ix_beachforecastlisthistory_id'), 'beachforecastlisthistory', ['id'], unique=False)
    op.create_index(op.f('ix_beachforecastlisthistory_ocean'), 'beachforecastlisthistory', ['ocean'], unique=False)
    op.create_index(op.f('ix_beachforecastlisthistory_region'), 'beachforecastlisthistory', ['region'], unique=False)
    op.add_column('beachforecastlist', sa.Column('beach_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_beachforecastlist_beach_id'), 'beachforecastlist', ['beach_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_beachforecastlist_beach_id'), table_name='beachforecastlist')
    op.drop_column('beachforecastlist', 'beach_id')
    op.drop_index(op.f('ix_beachforecastlisthistory_region'), table_name='beachforecastlisthistory')
    op.drop_index(op.f('ix_beachforecastlisthistory_ocean'), table_name='beachforecastlisthistory')
    op.drop_index(op.f('ix_beachforecastlisthistory_id'), table_name='beachforecastlisthistory')
    op.drop_index(op.f('ix_beachforecastlisthistory_beach_id'), table_name='beachforecastlisthistory')
    op.drop_index(op.f('ix_beachforecastlisthistory_beach'), table_name='beachforecastlisthistory')
    op.drop_table('beachforecastlisthistory')
    # ### end Alembic commands ###
