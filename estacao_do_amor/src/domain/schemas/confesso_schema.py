from pydantic import BaseModel


class Confesso(BaseModel):
    confissao: str
    user: str | None