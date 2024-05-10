from sqlalchemy.orm import Session
#criar nova info de um veiculo
from model import Veiculo
#dados do veiculo fornecidos
from schemas import VeiculoSchema



# create veiculo data

#def define a funçao q recebe 2 argumentos
#db é uma instancia da classe session do sqlalchemy p interagir no bd
#veiculo é um objeto do tipo veiculoschema que contem os dados do veiculo a ser criado

def create_veiculo(db: Session, veiculo: VeiculoSchema):
    _veiculo = Veiculo(fuel_rate=veiculo.fuel_rate, gps_speed=veiculo.gps_speed)
    #criando novo objeto veiculo com os valores de fuel rate n gps speed fornecido no objeto veiculo
    db.add(_veiculo)
    #add o objeto _veiculo no bd.
    db.commit()
    #confirma a alteração no bd
    db.refresh(_veiculo)
    #atualiza o objeto _veiculo com os novos valores do bd
    return _veiculo
    #retorna ao objeto _veiculo imediatamente