"""DateTime table add timezone=True

Revision ID: 1c1f8ab83eab
Revises: 3f7bf2552a2a
Create Date: 2023-08-30 14:52:58.817107

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1c1f8ab83eab"
down_revision: Union[str, None] = "3f7bf2552a2a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "planters", "register_date", type_=sa.DateTime(timezone=True), nullable=True
    )
    op.alter_column("planter_works", "sowing_date", type_=sa.DateTime(timezone=True))
    op.alter_column("planter_works", "deadline", type_=sa.DateTime(timezone=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "planters", "register_date", type_=sa.DateTime(timezone=False), nullable=True
    )
    op.alter_column("planter_works", "sowing_date", type_=sa.DateTime(timezone=False))
    op.alter_column("planter_works", "deadline", type_=sa.DateTime(timezone=False))
    # ### end Alembic commands ###
