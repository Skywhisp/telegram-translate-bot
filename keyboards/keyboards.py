from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

languages = {
    "🇷🇺": "ru",
    "🇺🇸": "en",
    "🇪🇸": "es",
    "🇨🇳": "zh",
    "🇫🇷": "fr"
}

async def show_language_keyboard(message):
    buttons = [
        InlineKeyboardButton(text=lang, callback_data=lang_code)
        for lang, lang_code in languages.items()
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=[buttons])
    await message.answer("Выберите язык для перевода:", reply_markup=keyboard)