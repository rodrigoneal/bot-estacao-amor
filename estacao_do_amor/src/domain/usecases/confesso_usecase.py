from typing import Generator
from estacao_do_amor.src.domain.repositories.confesso_repository import (
    ConfessoRepository,
)
from estacao_do_amor.src.domain.schemas.confesso_schema import Confesso


async def create(repository: ConfessoRepository, confesso_schema: Confesso):
    return await repository.create(confesso_schema)


async def read(
    repository: ConfessoRepository,
) -> Generator[Confesso, None, None]:
    confesso_model = await repository.read()
    for confesso in confesso_model:
        yield Confesso.model_validate(confesso)
