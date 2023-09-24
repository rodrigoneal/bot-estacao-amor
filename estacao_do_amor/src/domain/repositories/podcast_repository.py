from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from estacao_do_amor.src.domain.model import PodcastModel
from estacao_do_amor.src.domain.repositories.abstract_repository import (
    AbstractReposity,
)
from estacao_do_amor.src.domain.schemas.podcast_schema import Podcast


class PodcastRepository(AbstractReposity):
    def __init__(
        self, async_session_maker: async_sessionmaker[AsyncSession] = None
    ) -> None:
        self.async_session_maker = async_session_maker

    async def create(self, podcast: Podcast):
        podcast_model = PodcastModel(**podcast.model_dump())
        async with self.async_session_maker() as session:
            session.add(podcast_model)
            await session.commit()
