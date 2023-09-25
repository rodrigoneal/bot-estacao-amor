from pydantic import BaseModel


class Cerveja(BaseModel):
    user_id: int
    user_name: str
    data: str