"""Add total column in PlanterTray

Revision ID: e1d3a84b8665
Revises: 1c1f8ab83eab
Create Date: 2023-08-30 18:20:53.935672

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e1d3a84b8665'
down_revision: Union[str, None] = '1c1f8ab83eab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planter_trays', sa.Column('total', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('planter_trays', 'total')
    # ### end Alembic commands ###
