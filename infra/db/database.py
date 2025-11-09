
from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)
from typing import AsyncGenerator

from infra.config import settings
from infra.db.models import Base

engine = create_async_engine(
    settings.db_url,
    future=True
)

async_session_factory = async_sessionmaker(bind=engine, class_=AsyncSession,
                                           expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
