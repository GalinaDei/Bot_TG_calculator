from config import dp
import text
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from lib import*

@dp.message_handler(commands=['start'])
async def on_start(message: Message):
    await message.answer(text=f'{message.from_user.first_name}'f'{text.greeting}')


@dp.message_handler(commands=['sum', 'sub', 'mult', 'div', 'exp', 'square'])
async def get_command(message: Message):
    global sum_score
    global sub_score
    global mult_score
    global div_score
    global exp_score
    global squa_score
    if message.text == '/sum':
        sum_score = True
        sub_score = False
        mult_score = False
        div_score = False
        exp_score = False
        squa_score = False
        await message.answer(f'{message.from_user.first_name},' f' введите оба слагаемых через пробел')

    if message.text == '/sub':
        sum_score = False
        sub_score = True
        mult_score = False
        div_score = False
        exp_score = False
        squa_score = False
        await message.answer(f'{message.from_user.first_name},' f' введите уменьшаемый и '
                             f'вычитаемый операнды через пробел')

    if message.text == '/mult':
        sum_score = False
        sub_score = False
        mult_score = True
        div_score = False
        exp_score = False
        squa_score = False
        await message.answer(f'{message.from_user.first_name},' f' введите оба множителя через пробел')

    if message.text == '/div':
        sum_score = False
        sub_score = False
        mult_score = False
        div_score = True
        exp_score = False
        squa_score = False
        await message.answer(f'{message.from_user.first_name},' f' введите делимое и делитель через пробел')

    if message.text == '/exp':
        sum_score = False
        sub_score = False
        mult_score = False
        div_score = False
        exp_score = True
        squa_score = False
        await message.answer(f'{message.from_user.first_name},' f' введите основание и показатель степени через пробел')

    if message.text == '/square':
        sum_score = False
        sub_score = False
        mult_score = False
        div_score = False
        exp_score = False
        squa_score = True
        await message.answer(f'{message.from_user.first_name},' f' введите подкоренное число')

@dp.message_handler()
async def calc(message: Message):
    str = message.text.split()
    if sum_score:
        if str[0].replace('.','').strip(' .,-').isdigit() and str[1].replace('.','').strip(' .,-').isdigit():
            await message.answer(f"{summ(float(str[0].strip(' .,')), float(str[1].strip(' .,')))}")
        else:
            await message.answer(f'Тут что-то не так! Введите числа через пробел: ')
            pass

    if sub_score:
        if str[0].replace('.','').strip(' .,-').isdigit() and str[1].replace('.','').strip(' .,-').isdigit():
            await message.answer(f"{subb(float(str[0].strip(' .,')), float(str[1].strip(' .,')))}")
        else:
            await message.answer(f'Тут что-то не так! Введите числа через пробел: ')
            pass

    if mult_score:
        if str[0].replace('.','').strip(' .,-').isdigit() and str[1].replace('.','').strip(' .,-').isdigit():
            await message.answer(f"{multip(float(str[0].strip(' .,')), float(str[1].strip(' .,')))}")
        else:
            await message.answer(f'Тут что-то не так! Введите числа через пробел: ')
            pass

    if div_score:
        if str[0].replace('.','').strip(' .,-').isdigit() and str[1].replace('.','').strip(' .,-').isdigit():
            await message.answer(f"{divis(float(str[0].strip(' .,')), float(str[1].strip(' .,')))}")
        else:
            await message.answer(f'Тут что-то не так! Введите числа через пробел: ')
            pass

    if exp_score:
        if str[0].replace('.','').strip(' .,-').isdigit() and str[1].replace('.','').strip(' .,-').isdigit():
            await message.answer(f"{expon(float(str[0].strip(' .,')), float(str[1].strip(' .,')))}")
        else:
            await message.answer(f'Тут что-то не так! Введите числа через пробел: ')
            pass

    if squa_score:
        if str[0].replace('.','').strip(' .,-').isdigit():
            await message.answer(f"{square(float(str[0].strip(' .,')))}")
        else:
            await message.answer(f'Тут что-то не так! Введите числа через пробел: ')
            pass