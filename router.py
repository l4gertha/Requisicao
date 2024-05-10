from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import VeiculoSchema, RequestVeiculo, Response
import creating

#https://stackoverflow.com/questions/45020963/modulenotfounderror-no-module-named-models

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/create')
async def create(request: RequestVeiculo, db: Session = Depends(get_db)):
    creating.create_veiculo(db, veiculo=request.parameter)
    return Response(code=200, status="Ok", message="Veiculo criado com sucesso!").dict(exclude_none=True)

