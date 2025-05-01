from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keys.key import kb_start, kb_type, kb_days
from loader import router, cursor, con, scheduler, bot
from aiogram import F
from script.napominalka import napominalka_update


class Form_task(StatesGroup):
    id = State()
    task = State()
    time = State()
    type = State()
    date = State()
    days = State()


@router.message(F.text == "Добавить напоминалку")
async def handle_message(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await state.update_data(id=user_id)
    await state.set_state(Form_task.task)
    await message.answer('Введите вашу напоминалку', reply_markup=types.ReplyKeyboardRemove())


@router.message(Form_task.task)
async def get_task(message: Message, state: FSMContext):
    await state.update_data(task=message.text)
    await state.set_state(Form_task.time)
    await message.answer('Теперь введите время, когда будет приходить сообщение')


@router.message(Form_task.time)
async def get_time(message: Message, state: FSMContext):
    await state.update_data(time=message.text)
    await state.set_state(Form_task.type)
    builder = ReplyKeyboardBuilder()
    for button in kb_type:
        builder.add(button)
    builder.adjust(1)
    await message.answer(
        text='Теперь выбери формат отправки сообщения.',
        reply_markup=builder.as_markup(resize_keyboard=True))


@router.message(Form_task.type)
async def get_type(message: Message, state: FSMContext):
    print(354354)
    type_mes = message.text
    await state.set_state(Form_task.date)
    await state.update_data(type=message.text)
    if type_mes == 'В определённый день недели':
        builder = ReplyKeyboardBuilder()
        for button in kb_days:
            builder.add(button)
        builder.adjust(1)
        await message.answer(
            text='Выберете дни недели.',
            reply_markup=builder.as_markup(resize_keyboard=True))


    if type_mes == 'В один определённый день':
        await message.answer('Выберете день')
        await state.set_state(Form_task.date)
    if type_mes == 'Ежедневно':
        data = await state.get_data()
        if data['type'] == 'Ежедневно':
            await state.update_data(type='Ежедневно')
            data['days'] = '_'
            data['date'] = '_'
            id = data['id']
            task = data['task']
            time = data['time']
            type = data['type']
            date = data['date']
            days = data['days']

            user_id = message.from_user.id
            task_id = scheduler.add_job(napominalka_update,
                                        trigger='interval',
                                        seconds=2,
                                        kwargs={'user_id': user_id, 'bot': bot})
            id_task = task_id.id
            cursor.execute('INSERT INTO users (id, task, time, type, date, days, id_task) VALUES (?,?,?,?,?,?,?)',
                           (id, task, time, type, date, days, id_task))
            con.commit()
            await state.clear()
            await message.answer('Ваша напоминалка готова!')



@router.message(Form_task.date)
async def get_date(message: Message, state: FSMContext):
    data = await state.get_data()
    print(data)
    data['kek'] = 234

    if data['type'] == 'Ежедневно':
        await state.update_data(type='Ежедневно')
        data['days'] = '_'
        data['date'] = '_'

    if data['type'] == 'В определённый день недели':
        await state.update_data(days=message.text)
        data['date']='_'

    if data['type'] == 'В один определённый день':
        await state.update_data(date=message.text)
        data['days'] = '_'
    id = data['id']
    task = data['task']
    time = data['time']
    type = data['type']
    date = data['date']
    days = data['days']
    user_id = message.from_user.id
    task_id = scheduler.add_job(napominalka_update,
                                trigger='interval',
                                seconds=2,
                                kwargs={'user_id': user_id, 'bot': bot})
    id_task = task_id.id
    cursor.execute('INSERT INTO users (id, task, time, type, date, days, id_task) VALUES (?,?,?,?,?,?,?)',
                   (id, task, time, type, date, days, id_task))
    await state.clear()
    con.commit()
    await message.answer('Ваша напоминалка готова!')
