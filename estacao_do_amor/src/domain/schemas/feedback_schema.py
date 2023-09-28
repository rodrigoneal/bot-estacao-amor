from pydantic import BaseModel, field_validator

from estacao_do_amor.src.domain.schemas import ReadBase


class FeedBack(BaseModel):
    user_id: int
    user_name: str
    feedback: str
    tipo_sugestao: str
    pode_contato: bool

class FeedBackRead(ReadBase):    
    user_name: str
    feedback: str
    tipo_sugestao: str
    pode_contato: str
    @field_validator("pode_contato", mode="before")
    @classmethod
    def responder_feedback(cls, v) -> str:
        return "Pode" if v is True else "Não"