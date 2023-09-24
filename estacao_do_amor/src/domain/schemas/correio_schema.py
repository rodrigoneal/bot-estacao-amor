from pydantic import BaseModel


class Correio(BaseModel):
    remetente: str | None
    destinatario: str
    mensagem: str
