import logging
from aiogram import Bot, Dispatcher, types  # Исправленный импорт
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import Database  # Импортируем наш класс для работы с базой данных

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация бота и диспетчера
API_TOKEN = '7339010392:AAErvcJ6GV_lzARBlxVhs1C8vQEuRJn6Rg8YOUR_BOT_API_TOKEN'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Инициализация базы данных
db = Database(
    dbname="your_dbname",
    user="your_username",
    password="your_password",
    host="localhost",
    port=5432
)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот для игры 'Правда или действие'. Напиши @brumbabot в любом чате, чтобы начать игру!")

# Обработчик инлайн-запросов
@dp.inline_handler()
async def inline_query_handler(inline_query: types.InlineQuery):
    # Создаем клавиатуру с кнопками "Правда", "Действие" и "Добавить свой вопрос"
    keyboard = InlineKeyboardMarkup(row_width=2)
    truth_button = InlineKeyboardButton(text="Правда", callback_data="truth")
    dare_button = InlineKeyboardButton(text="Действие", callback_data="dare")
    add_question_button = InlineKeyboardButton(text="Добавить свой вопрос", callback_data="add_question")
    keyboard.add(truth_button, dare_button, add_question_button)

    # Создаем инлайн-результат
    result = types.InlineQueryResultArticle(
        id="1",
        title="Правда или действие",
        input_message_content=types.InputTextMessageContent("Выбери 'Правда' или 'Действие'!"),
        reply_markup=keyboard
    )

    await bot.answer_inline_query(inline_query.id, [result])

# Обработчик callback-запросов
@dp.callback_query_handler(lambda c: c.data in ['truth', 'dare'])
async def process_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)

    if callback_query.data == 'truth':
        question = db.get_random_question()
        await bot.send_message(callback_query.from_user.id, f"Правда: {question}")
    elif callback_query.data == 'dare':
        question = db.get_random_question()
        await bot.send_message(callback_query.from_user.id, f"Действие: {question}")

# Обработчик для кнопки "Добавить свой вопрос"
@dp.callback_query_handler(lambda c: c.data == 'add_question')
async def add_question_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    # Здесь будет реализация добавления вопроса
    pass

# Запуск бота
if __name__ == '__main__':
    try:
        Dispatcher.start_polling(dp, skip_updates=True)
    finally:
        db.close()  # Закрываем соединение с базой данных при завершении работы бота