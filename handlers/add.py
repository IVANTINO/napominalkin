from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keys.key import kb_start, kb_type
from loader import router, cursor, con, scheduler, bot
from aiogram import F
from script.napominalka import napominalka_update


class Form_task(StatesGroup):
    id = State()
    task = State()
    time = State()
    type = State()
    date = State()


@router.message(F.text == "Добавить напоминалку")
async def handle_message(message: Message, state: FSMContext):
    user_id = message.from_user.id

    await state.set_state(Form_task.task)
    await message.answer('Введите вашу напоминалку', reply_markup=types.ReplyKeyboardRemove())


@router.message(Form_task.task)
async def get_task(message: Message, state: FSMContext):
    await state.update_data(task=message.text)
    await state.set_state(Form_task.time)
    await message.answer('Теперь введите время, когда будет приходить сообщение')


@router.message(Form_task.time)
async def get_time(message: Message, state: FSMContext):
    await state.update_data(task=message.text)
    await state.set_state(Form_task.type)
    await message.answer('Теперь выберите формат отправки сообщения')


@router.message(Form_task.type)
async def get_type(message: Message, state: FSMContext):
    await state.update_data(task=message.text)
    await state.set_state(Form_task.type)
    await message.answer('Введите дни')

@router.message(Form_task.type)
async def get_type(message: Message, state: FSMContext):
    await state.update_data(task=message.text)
    await state.set_state(Form_task.date)
    if message.answer == 'Ежедневно':
        await message.answer('Ваша напоминалка готова!')

