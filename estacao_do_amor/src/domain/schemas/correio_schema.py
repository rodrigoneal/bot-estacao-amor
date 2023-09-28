from pydantic import BaseModel, ConfigDict


class CorreioBase(BaseModel):
    remetente: str | None
    destinatario: str
    mensagem: str


class Correio(CorreioBase):
    user_id: int
    user_name: str

class CorreioRead(CorreioBase):
    model_config = ConfigDict(from_attributes=True)

