import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from sqlalchemy import text

from bot.handlers import common
from bot.middlewares.access import AccessMiddleware
from infra.config import settings
from infra.db.database import engine, init_db
from infra.logger import setup_logging


async def main():

    # Logging setup
    setup_logging()
    logging.info("Bot starts...")

    # Database connection test
    try:
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
        logging.info("Database successfully connected")
    except Exception as e:
        logging.exception(f"Database connection error:\n{e}")
        return

    # Database initialization
    await init_db()
    logging.info("Database and tables are successfuly created")

    # Bot initialization
    bot = Bot(token=settings.BOT_TOKEN,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())

    # Handlers registration
    dp.include_routers(
        # admin.router,
        # schedule.router,
        common.router,
    )

    # Add user access middleware
    dp.message.middleware(AccessMiddleware())

    # Log notification
    logging.info("Bot started successfully. Waiting for messages...")

    # Long polling start
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped manually.")
