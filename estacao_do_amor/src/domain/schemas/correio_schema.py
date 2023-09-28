from pydantic import BaseModel

from estacao_do_amor.src.domain.schemas import ReadBase


class CorreioBase(BaseModel):
    remetente: str | None
    destinatario: str
    mensagem: str


class Correio(CorreioBase):
    user_id: int
    user_name: str

class CorreioRead(ReadBase, CorreioBase):
    pass

