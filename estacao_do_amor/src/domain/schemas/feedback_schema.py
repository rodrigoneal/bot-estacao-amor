from pydantic import BaseModel, ConfigDict, computed_field, field_validator


class FeedBack(BaseModel):
    user_id: int
    user_name: str
    feedback: str
    tipo_sugestao: str
    pode_contato: bool

class FeedBackRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user_name: str
    feedback: str
    tipo_sugestao: str
    pode_contato: str
    @field_validator("pode_contato", mode="before")
    @classmethod
    def responder_feedback(cls, v) -> str:
        return "Pode" if v is True else "Não"