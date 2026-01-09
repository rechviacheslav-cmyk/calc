from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import botcalculator.keybodrf as kb
import time
router = Router()
class Mats(StatesGroup):
    one = State()
    two = State()
    die = State()

@router.message(Command('start'))
async def start(message: Message):
    await message.answer("Привет это бот калькулятор для калькулятора пропишите\n /calc")
@router.message(Command('calc'))
async def calc(message: Message, state: FSMContext):
    await message.answer("Введите первое число:")
    await state.set_state(Mats.one)
@router.message(Mats.one)
async def one_calc(message: Message, state: FSMContext):
    try:
        await state.update_data(one=int(message.text))
    except ValueError:
        await message.answer("Введите число:")
        return
    await message.answer("Введите второе число")
    await state.set_state(Mats.two)
@router.message(Mats.two)
async def two_calc(message: Message, state: FSMContext):
    try:
        await state.update_data(two=int(message.text))
    except ValueError:
        await message.answer("Введите число")
        return
    await message.answer("Введите действие (+, -, /, *)", reply_markup=kb.main)
    await state.set_state(Mats.die)
@router.message(Mats.die)
async def three_calc(message: Message, state: FSMContext):
    await state.update_data()
    data = await state.get_data()
    die = message.text
    one = int(data['one'])
    two = int(data['two'])
    if die not in ('+', '-', '*', '/'):
        await message.answer("Введите действие ('+', '-', '*', '/')", reply_markup=kb.main)
        return
    if die == "+":
        result = one + two
    elif die == "-":
        result = one - two
    elif die == "/":
        try:
            result = one / two
        except ZeroDivisionError:
            await message.answer(f"На ноль делить нельзя ошибка:\n {ZeroDivisionError}")
    elif die == "*":
        result = one * two
    await message.answer(f"Ваш результат: {result}")
    await state.clear()

