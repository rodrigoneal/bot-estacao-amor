from pydantic import BaseModel


class Correio(BaseModel):
    remetente: str | None
    destinatario: str
    mensagem: str
    user_id: int
    user_name: str
