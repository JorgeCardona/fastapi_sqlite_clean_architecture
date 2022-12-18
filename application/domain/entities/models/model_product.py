from sqlalchemy import Column, Integer, String
from configuration.environment.env import Environment

class Product(Environment.Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    categorie = Column(String(256))
    price = Column(Integer)
    """
    def __get__item(self, key):
        return self.__dict__[key]
    """
        