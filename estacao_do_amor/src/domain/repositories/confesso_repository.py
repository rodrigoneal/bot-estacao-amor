from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from estacao_do_amor.src.domain.model import ConfissaoModel
from estacao_do_amor.src.domain.repositories.abstract_repository import \
    AbstractReposity
from estacao_do_amor.src.domain.schemas.confesso_schema import Confesso


class ConfessoRepository(AbstractReposity):
    def __init__(
        self, async_session_maker: async_sessionmaker[AsyncSession] = None
    ) -> None:
        self.async_session_maker = async_session_maker

    async def create(self, confesso: Confesso) -> ConfissaoModel:
        confesso_model = ConfissaoModel(**confesso.model_dump())
        async with self.async_session_maker() as session:
            session.add(confesso_model)
            await session.commit()

    async def read(self) -> list[ConfissaoModel]:
        async with self.async_session_maker() as session:
            query = select(ConfissaoModel)
            result = await session.execute(query)
            return result.scalars().all()
