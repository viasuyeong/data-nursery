from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship


from utils.database import BaseModel, AppModelBase
from src.planter.models import Planter


class User(BaseModel):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    login_id = Column(String(length=20), unique=True, index=True)
    password = Column(String)
    code = Column(String(length=2), default="01")

    user_farm_house = relationship(
        "FarmHouse",
        uselist=False,
        back_populates="farm_house_user",
        primaryjoin="User.id == FarmHouse.owner_id",
    )


class FarmHouse(BaseModel):
    __tablename__ = "farm_houses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=255), unique=True, index=True)
    nursery_number = Column(String(length=244), unique=True, index=True)
    address = Column(Text)
    owner_id = Column(Integer, ForeignKey("users.id"))
    phone = Column(String(length=20))

    farm_house_user = relationship("User", back_populates="user_farm_house")
    farm_house_planter = relationship(
        "Planter",
        uselist=False,
        back_populates="planter_farm_house",
        primaryjoin="FarmHouse.id == Planter.farm_house_id",
    )