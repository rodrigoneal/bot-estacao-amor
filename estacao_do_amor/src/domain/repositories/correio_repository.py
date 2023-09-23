from sqlalchemy import delete, select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from estacao_do_amor.src.domain.model import PodcastModel
from estacao_do_amor.src.domain.repositories.abstract_repository import \
    AbstractReposity
from estacao_do_amor.src.domain.schemas.correio_schema import Correio


class CorreioRepository(AbstractReposity):
    def __init__(
        self, async_session_maker: async_sessionmaker[AsyncSession] = None
        
    ) -> None:
        self.async_session_maker = async_session_maker
    async def create(self, correio: Correio):
        podcast_model = PodcastModel(**correio.model_dump())
        async with self.async_session_maker() as session:
            session.add(podcast_model)
            await session.commit()