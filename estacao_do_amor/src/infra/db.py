from functools import lru_cache

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from estacao_do_amor.src.domain.model import Base


class Settings():
    database_url: str = "sqlite+aiosqlite:///estacao_do_amor.db"

@lru_cache
def get_settings():
    return Settings()


settings = get_settings()


engine = create_async_engine(settings.database_url)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
