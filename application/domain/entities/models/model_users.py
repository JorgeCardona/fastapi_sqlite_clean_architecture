from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from configuration.environment.env import Environment

class User(Environment.Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    #items = relationship("Product", back_populates="owner")