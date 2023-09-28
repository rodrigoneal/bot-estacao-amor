from estacao_do_amor.src.domain.repositories.cerveja_repository import \
    CervejaRepository
from estacao_do_amor.src.domain.schemas.cerveja_schema import Cerveja


async def create(repository: CervejaRepository, cerveja_schema: Cerveja):
    await repository.create(cerveja_schema)

async def read(repository: CervejaRepository):
    cerveja_model = await repository.read()
    for cerveja in cerveja_model:
        yield Cerveja.model_validate(cerveja)