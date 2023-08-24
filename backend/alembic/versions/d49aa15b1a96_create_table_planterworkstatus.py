"""create table PlanterWorkStatus

Revision ID: d49aa15b1a96
Revises: 11eb52d923a7
Create Date: 2023-08-24 00:46:48.462128

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd49aa15b1a96'
down_revision: Union[str, None] = '11eb52d923a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planter_work_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('planter_work_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(length=7), nullable=True),
    sa.Column('is_del', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['planter_work_id'], ['planter_works.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_planter_work_status_id'), 'planter_work_status', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_planter_work_status_id'), table_name='planter_work_status')
    op.drop_table('planter_work_status')
    # ### end Alembic commands ###
