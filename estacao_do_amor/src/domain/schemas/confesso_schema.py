from pydantic import BaseModel


class Confesso(BaseModel):
    mensagem: str
    user_name: str | None
    user_id: int | None