from estacao_do_amor.src.domain.schemas import ReadBase


class Confesso(ReadBase):
    mensagem: str
    user_name: str | None
    user_id: int | None