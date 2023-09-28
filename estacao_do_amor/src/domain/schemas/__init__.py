from pydantic import BaseModel, ConfigDict


class ReadBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)