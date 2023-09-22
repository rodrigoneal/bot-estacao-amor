import sqlite3
from pathlib import Path

import pytest
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from estacao_do_amor.src.domain.model import Base
from estacao_do_amor.src.domain.repositories.repositories import Repository
from estacao_do_amor.src.feed.feed_rss import AnchorFeed

URI = r"sqlite+aiosqlite:///teste.db"

@pytest.fixture
def get_repository(create_table):
    return  Repository(create_table)

@pytest.fixture()
async def create_engine():
    engine = create_async_engine(URI)
    return engine
@pytest.fixture()
async def create_table(create_engine):
    engine = create_engine
    async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        yield async_session_maker
        await conn.run_sync(Base.metadata.drop_all)
        Path("teste.db").unlink(missing_ok=True)

@pytest.fixture
def get_cursor():
    conn = sqlite3.connect('teste.db')
    cursor = conn.cursor()
    return cursor


@pytest.fixture
def first_episode():
    anchor_feed = AnchorFeed()
    episodes = anchor_feed.podcast_episodes()
    return episodes.episodes[-1]