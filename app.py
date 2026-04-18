import telebot
from telebot import types

TOKEN = "8169646463:AAGwFa2am7mlerbJJyS1wwmDy1LmFWwyles"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("💳 خرید اشتراک", "📋 تعرفه پلن‌ها")
    kb.row("🧾 ارسال رسید", "🎧 پشتیبانی")

    bot.send_message(
        message.chat.id,
        "سلام 👋 به فروشگاه VPN خوش اومدی",
        reply_markup=kb
    )

@bot.message_handler(func=lambda m: True)
def menu(message):

    if message.text == "💳 خرید اشتراک":
        txt = """
پلن‌ها:

1 گیگ / 1 ماهه = 400,000
2 گیگ / 1 ماهه = 780,000
3 گیگ / 1 ماهه = 1,150,000
4 گیگ / 1 ماهه = 1,560,000
5 گیگ / 1 ماهه = 1,990,000
6 گیگ / 1 ماهه = 2,390,000

برای خرید پیام بده:
@Hjpa33
"""
        bot.send_message(message.chat.id, txt)

    elif message.text == "📋 تعرفه پلن‌ها":
        bot.send_message(message.chat.id, "برای مشاهده قیمت‌ها روی خرید اشتراک بزن")

    elif message.text == "🧾 ارسال رسید":
        txt = """
مبلغ را به کارت زیر واریز کنید:

5859831840357304

به نام: هما پاکزاد

سپس رسید را به آیدی زیر ارسال کنید:
@Hjpa33
"""
        bot.send_message(message.chat.id, txt)

    elif message.text == "🎧 پشتیبانی":
        bot.send_message(message.chat.id, "پشتیبانی: @Hjpa33")

bot.infinity_polling()
