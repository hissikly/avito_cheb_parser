from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from datetime import *


from parse_service import *
from text import *
from keyboards import *

TOKEN = "6167057957:AAFoxaYHHH2LNejD6SiaInYAAxnRPbJB8CE"
bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class StateParam(StatesGroup):
    title = State()


@dp.message_handler(commands=["start"])
async def cmd_start(mes: types.Message):
    await mes.answer(GREETING, parse_mode='html', reply_markup=start_kb())


@dp.message_handler(commands=['today'])
async def cmd_today(mes: types.Message):
    await mes.answer("Подождите пару секунд...", reply_markup=types.ReplyKeyboardRemove())
    await mes.answer("Итак афиша на сегодня", reply_markup=create_keyboard(get_all_titles(f"https://afisha.cheb.ru/kino/?cdate={date.today()}&sort=")))
    await StateParam.title.set()


@dp.callback_query_handler(lambda callback_query: callback_query.data in cut_titles, state=StateParam.title)
async def today_info(callback: types.CallbackQuery, state: FSMContext):
    info = get_all_info(f"https://afisha.cheb.ru/kino/?cdate={date.today()}&sort=", callback.data, True)
    if info:
        await callback.message.answer(transform_text(info))
    else:
        await callback.message.answer("Извините не нашлось кинофильма с таким названием")
    await state.finish()


@dp.message_handler(commands=['tommorow'])
async def cmd_today(mes: types.Message):
    await mes.answer("Подождите пару секунд...")
    await mes.answer("Итак афиша на завтра", reply_markup=create_keyboard(get_all_titles(f"https://afisha.cheb.ru/kino/?cdate={date.today() + timedelta(days=1)}&sort=")))
    await StateParam.title.set()


@dp.callback_query_handler(lambda callback_query: callback_query.data in cut_titles, state=StateParam.title)
async def tommorow_info(callback: types.CallbackQuery, state: FSMContext):
    info = get_all_info(f"https://afisha.cheb.ru/kino/?cdate={date.today() + timedelta(days=1)}&sort=", callback.data, False)
    if info:
        await callback.message.answer(transform_text(info))
    else:
        await callback.message.answer("Извините не нашлось кинофильма с таким названием")
    await state.finish()


@dp.message_handler()
async def get_random_mes(mes: types.Message):
    await mes.answer('Прости, я тебя не понимяу :(', reply_markup=start_kb())


if __name__ == "__main__":
    executor.start_polling(dp)
