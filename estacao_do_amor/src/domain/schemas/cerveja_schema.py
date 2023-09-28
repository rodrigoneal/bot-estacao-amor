from pydantic import BaseModel

from estacao_do_amor.src.domain.schemas import ReadBase


class Cerveja(ReadBase):
    user_id: int
    user_name: str
    data: str