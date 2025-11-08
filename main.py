import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from infra.config import settings
from infra.logger import setup_logging
from bot.handlers import admin, schedule, common


async def main():
    # Logging setup
    setup_logging()
    logging.info("Bot starts...")

    # Bot initialization
    bot = Bot(token=settings.BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())

    # Handlers registration
    dp.include_routers(
        admin.router,
        schedule.router,
        common.router,
    )

    # Log notification
    logging.info("Bot started successfully. Waiting for messages...")

    # Long polling start
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped manually.")
