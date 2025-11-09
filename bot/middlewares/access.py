import logging
from sqlalchemy import select
from aiogram import BaseMiddleware, Bot
from aiogram.types import Message

from infra.db.models import User
from infra.db.database import async_session_factory


class AccessMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Message, data: dict):
        async with async_session_factory() as session:
            result = await session.execute(select(User).where(
                User.id == event.from_user.id))
            user = result.scalar_one_or_none()

        if not user:
            bot: Bot = data["bot"]
            await bot.send_message(event.chat.id,
                                   text="У вас нет доступа к боту.")
            logging.warning("Unauthorized user: %s",
                            event.from_user.id)
            return

        return await handler(event, data)
