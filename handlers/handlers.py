from aiogram import Router, types
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from keyboards.keyboards import show_language_keyboard, languages

from services.ya_translate_api import get_translation

router = Router()

class LearningState(StatesGroup):
    waiting_for_word = State()
    waiting_for_language = State()

@router.message(CommandStart())
async def start_command(message: types.Message):
    await show_language_keyboard(message)

@router.callback_query(lambda c: c.data in languages.values())
async def set_language(callback_query: types.CallbackQuery, state: FSMContext):
    selected_language = callback_query.data
    await state.update_data(language=selected_language)
    await callback_query.answer(f"Язык для перевода установлен на: {list(languages.keys())[list(languages.values()).index(selected_language)]}")
    await state.set_state(LearningState.waiting_for_word)
    await callback_query.message.answer("Введите текст для перевода:")

@router.message(StateFilter(LearningState.waiting_for_word))
async def handle_word(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    translation_language = user_data.get("language", "en")

    texts = message.text

    translation = get_translation(texts, translation_language)

    if translation:
        await message.answer(translation)
    else:
        await message.answer("Не удалось получить перевод для текста.")

    await show_language_keyboard(message)