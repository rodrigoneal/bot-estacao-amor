from estacao_do_amor.src.domain.repositories.cerveja_repository import \
    CervejaRepository
from estacao_do_amor.src.domain.schemas.cerveja_schema import Cerveja


async def create(repository: CervejaRepository, cerveja_schema: Cerveja):
    await repository.create(cerveja_schema)
