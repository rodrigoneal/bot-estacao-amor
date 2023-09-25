from estacao_do_amor.src.domain.model import CorreioModel
from estacao_do_amor.src.domain.repositories.correio_repository import \
    CorreioRepository
from estacao_do_amor.src.domain.schemas.correio_schema import Correio


async def create(
    repository: CorreioRepository, correio_schema: Correio
) -> CorreioModel:
    podcast_model = await repository.create(correio_schema)
    return podcast_model
