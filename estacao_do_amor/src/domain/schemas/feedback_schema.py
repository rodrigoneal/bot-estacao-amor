from pydantic import BaseModel


class FeedBack(BaseModel):
    user_id: int
    user_name: str
    feedback: str
    tipo_sugestao: str
    pode_contato: bool