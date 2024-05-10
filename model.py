from sqlalchemy import Column, Integer, Float
from config import Base

#declarando tabela
class Veiculo(Base):
#declarando classe Veiculo para representar dados de veiculos no bd
    __tablename__ = 'Veiculo'
# colunas da tabela
    id = Column(Integer, primary_key=True)
    fuel_rate = Column(Float)  #
    gps_speed = Column(Float)