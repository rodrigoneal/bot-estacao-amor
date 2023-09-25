from estacao_do_amor.src.domain.repositories.confesso_repository import \
    ConfessoRepository
from estacao_do_amor.src.domain.schemas.confesso_schema import Confesso


async def create(repository: ConfessoRepository, confesso_schema: Confesso):
    return await repository.create(confesso_schema)
