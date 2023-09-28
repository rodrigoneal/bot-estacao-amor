from pydantic import BaseModel, ConfigDict



class CervejaBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user_name: str
    data: str


class Cerveja(CervejaBase):
    user_id: int


class CervejaRead(CervejaBase):
    pass
