from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from estacao_do_amor.src.domain.model import FeedBackModel
from estacao_do_amor.src.domain.repositories.abstract_repository import \
    AbstractReposity
from estacao_do_amor.src.domain.schemas.feedback_schema import FeedBack


class FeedBackRepository(AbstractReposity):
    def __init__(
        self, async_session_maker: async_sessionmaker[AsyncSession] = None
    ) -> None:
        self.async_session_maker = async_session_maker

    async def create(self, feedback: FeedBack) -> FeedBackModel:
        feedback_model = FeedBackModel(**feedback.model_dump())
        async with self.async_session_maker() as session:
            session.add(feedback_model)
            await session.commit()
