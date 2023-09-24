from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from estacao_do_amor.src.domain.model import ConfissaoModel
from estacao_do_amor.src.domain.repositories.abstract_repository import (
    AbstractReposity,
)
from estacao_do_amor.src.domain.schemas.confesso_schema import Confesso


class ConfessoRepository(AbstractReposity):
    async def create(self, confesso: Confesso) -> ConfissaoModel:
        async with async_sessionmaker() as session:
            confesso_model = ConfissaoModel(**confesso.model_dump())
            async with session.begin():
                session.add(confesso_model)
                return await session.commit()