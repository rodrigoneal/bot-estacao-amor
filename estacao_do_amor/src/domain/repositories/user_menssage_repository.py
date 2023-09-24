from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from estacao_do_amor.src.domain.model import CorreioModel, UserMessageModel
from estacao_do_amor.src.domain.repositories.abstract_repository import (
    AbstractReposity,
)
from estacao_do_amor.src.domain.schemas.correio_schema import Correio


class UserMessageRepository(AbstractReposity):
    def __init__(
        self, async_session_maker: async_sessionmaker[AsyncSession] = None
    ) -> None:
        self.async_session_maker = async_session_maker

    async def create(self, correio: Correio) -> CorreioModel:
        podcast_model = CorreioModel(**correio.model_dump())
        async with self.async_session_maker() as session:
            session.add(podcast_model)
            await session.commit()

    async def get_or_create(self, user_id: int):
        async with self.async_session_maker() as session:
            query = select(UserMessageModel).where(
                UserMessageModel.user_id == user_id
            )
            result = await session.execute(query)
            user_message = result.scalars().first()
            if user_message:
                return user_message
            user_message = UserMessageModel(user_id=user_id)
            session.add(user_message)
            await session.commit()
            await session.refresh(user_message)
            return user_message

    async def update(self, user_id: int):
        async with self.async_session_maker() as session:
            stmt = update(UserMessageModel).where(
                UserMessageModel.user_id == user_id
            )
            await session.execute(stmt)
            await session.commit()

    async def read(self, user_id: int):
        stmt = select(UserMessageModel).where(
            UserMessageModel.user_id == user_id
        )
        async with self.async_session_maker() as session:
            result = await session.execute(stmt)
            user_message = result.scalars().first()
            return user_message
