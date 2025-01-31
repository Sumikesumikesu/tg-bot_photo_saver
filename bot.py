import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from config_data.config import load_config, Config


async def main():

    config: Config = load_config()

    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    @dp.message(CommandStart())
    async def process_command_start(message: Message):
        await message.answer(text="Я бот, который сохраняет фото в директорию")

    @dp.message(F.photo)
    async def process_photo(message: Message):
        file_id = message.photo[-1].file_id

        file_info = await bot.get_file(file_id)
        file_path = file_info.file_path

        caption = message.caption

        save_folder = config.folder.path

        if caption:
            save_path = f'{save_folder}/{caption}.jpg'
        else:
            save_path = f'{save_folder}/{file_id}.jpg'

        await bot.download_file(file_path, save_path)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
