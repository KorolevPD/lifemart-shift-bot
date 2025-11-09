from aiogram.filters import Command
import logging
from aiogram.types import Message
from aiogram import Router


router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.reply("Привет!\nИспользуй команды для работы с расписанием.")
    logging.info("Пользователь %s начал работу с ботом.", message.from_user.id)
