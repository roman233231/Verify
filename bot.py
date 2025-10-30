from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# 🔑 ВСТАВ СВІЙ ТОКЕН ВІД @BotFather
TOKEN = "8238889887:AAH5zyMcQ8OzKbLXKfg2r4r5TSChQt6fb-s"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# 📨 Коли користувач надсилає запит на вступ у канал
@dp.chat_join_request_handler()
async def join_request_handler(update: types.ChatJoinRequest):
    user = update.from_user
    chat = update.chat

    # 🔔 Надсилаємо користувачу повідомлення
    await bot.send_message(
        user.id,
        f"Привіт, {user.first_name}! 👋\n"
        f"Дякуємо за запит на вступ у канал **{chat.title}**.\n\n"
        "Щоб підтвердити, що ви не бот, натисніть /start."
    )

    # ✅ Одразу приймаємо запит (можна прибрати, якщо хочеш схвалювати вручну)
    await update.approve()

# ▶️ Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp)
