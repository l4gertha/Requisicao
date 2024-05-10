
#import sys
#sys.path.insert(0, './src/')
from fastapi import FastAPI
import  model
#importa a biblio q contem a def das classes do sqlalchemy q representam o modelo de dados
from sqlalchemy import create_async_engine
#importa a instancia engine do sqlalchemy do arquivo config p/ conectar no bd
import  router

#importa a biblio q contem as rotas de aplicação

##CRIANDO AS TABELAS NO BD

#nao consegue mapear o endereço do banco
try:
  engine = create_async_engine("postgresql+asyncpg://laracamilly:postgres@localhost:7779/postgres", echo=True)
  print("oi")
  model.Base.metadata.create_all(bind=engine)
except NameError:
  print("")


#solicita o metodo create all no objeto metadata da classe base definida na biblio model, tendo engine como argumento
#isso cria toda tabela definida no modelo de dados no bd especificado pela enginss

#app = FastAPI()
#inicializa a aplicação web fastapi

#@app.get('/')
#define uma rota para o path raiz utilizando get method
# essa function é exec quando a raiz do server for acessada por um navegador ou cliente http
#async def home():
#    return "Welcome Home"
#é executada quando a rota raiz for acessada


#app.include_router(router.router, prefix="/Veiculo", tags=["Veiculo"])
##inclui rotas definidas no objeto apirouter na aplicação fastapi. define o prefixo
#para todas as rotas incluidas e adiciona a tag veiculo