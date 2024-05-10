from typing import Optional, TypeVar

from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class VeiculoSchema(BaseModel):
    id: Optional[int] = None
    fuel_rate: Optional[str] = None
    gps_speed: Optional[str] = None

    class Config:
        orm_mode = True


class RequestVeiculo(BaseModel):
    parameter: VeiculoSchema = Field(...)

class Response(BaseModel):
    code: int
    status: str
    message: str


