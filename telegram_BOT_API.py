import telebot

token = "1639212856:AAEgsVvqVJ8AQ-YF_aMKvwhQnndeZl6kIjk"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Привет")


bot.infinity_poling()
