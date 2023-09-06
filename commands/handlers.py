from config import dp, bot
from config.config import DEBUG
from database import User, Group
from keyboards import Keyboard
from utils.docParse import parseDocument

from aiogram import types
from aiogram.dispatcher import FSMContext, filters
from aiogram.dispatcher.filters.state import State, StatesGroup
import logging



from aiogram.utils.helper import Helper, HelperMode, ListItem


# Класс состояний
class Options(StatesGroup):
    enter_group = State()

# Хендлер на старт
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    try:
        # Получаем пользователя
        user = message.from_user
        
        # Лог сообщения
        logging.info(f'New message: User={user.id}, Message={message.text}')

        # Проверка на существование пользователя
        await User.exists(user.id)

        # Отправка ответа
        await bot.send_message(
            chat_id=user.id,
            text=f'👋 Здравствуйте, { user.first_name }!\n' + \
                '👨‍🏫 Я предназначен для упрощения работы с сайтом novsu.ru\n\n' + \
                '🧰 На данный момент я могу:\n' + \
                '📝 Просматривать существующие замены',
            reply_markup=Keyboard.main()
        )
    except Exception as error:
        print(f'[ Commands/Handlers/process_start_command ] Error: {error}')
        logging.error(error)

#
#
# Тронут фильтр
#
#

# Обработка события нажатия на кнопку "Просмотр замен"
#
# Допустимые варианты регулярного выражения:
#
# просмотр замен
# замена
# замены
#
@dp.message_handler(filters.Regexp('(просмотр замен|замен(а|ы))'))
async def checkReplacement(message: types.Message):
    # Получаем юзера
    user = await User.get( message.from_user.id )

    # Если группа установлена
    if not user.group_id is None and type(user.group_id) == int:
        return await message.answer(parseDocument(group))
    else:
        return await message.reply('❌ Для начала установите группу')

    

#
# Допустимые варианты регулярного выражения:
#
# выбор группы
# группа
#   
@dp.message_handler(filters.Regexp('(выбор группы|группа)'))
async def selectGroup(message: types.Message):
    # Устанавливаем состояние
    await Options.enter_group.set()
    
    return await message.reply(
        '✏️ Введите номер группы', 
        reply=False, 
        reply_markup=types.ReplyKeyboardRemove()
    )


#
#
# Тронута обработка и состояние
#
#

# Запись полученного номера группы 
@dp.message_handler(state=Options.enter_group)
async def input_group(message: types.Message, state: FSMContext):
    # Поиск группы
    group = await Group.exists( message.text.strip() )

    if bool(group):
        await User.update(user.id, group.id)
    else:
        return await message.reply('❌ Такой группы не существует')
    
    # Завершаем состояние
    await state.finish()

    return await message.answer(
        '✅ Номер группы успешно сохранен',
        reply=False,
        reply_markup=addButtons()
    )
