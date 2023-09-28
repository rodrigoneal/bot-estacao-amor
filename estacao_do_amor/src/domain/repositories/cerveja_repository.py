from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy import select
from estacao_do_amor.src.domain.model import CervejaModel
from estacao_do_amor.src.domain.repositories.abstract_repository import \
    AbstractReposity
from estacao_do_amor.src.domain.schemas.cerveja_schema import Cerveja


class CervejaRepository(AbstractReposity):
    def __init__(
        self, async_session_maker: async_sessionmaker[AsyncSession] = None
    ) -> None:
        self.async_session_maker = async_session_maker

    async def create(self, cerveja: Cerveja) -> CervejaModel:
        confesso_model = CervejaModel(**cerveja.model_dump())
        async with self.async_session_maker() as session:
            session.add(confesso_model)
            await session.commit()

    async def read(self) -> list[CervejaModel] | None:
        query = select(CervejaModel)
        async with self.async_session_maker() as session:
            result = await session.execute(query)
            return result.scalars().all()