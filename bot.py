import telebot

bot = telebot.TeleBot('1206667494:AAH8jcZQ5paiw3diBrA7JmTjMBRhens98EQ')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi you wrote meee!')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'hi' or message.text.lower() =='hello':
        bot.send_message(message.chat.id, 'Hii boss')
    elif message.text.lower() == 'bye':
        bot.send_message(message.chat.id, 'Bye Bye')
    elif message.text.lower() == 'love ya':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAANUXrxISplP8YynCkgX7Px4m3vJgNYAApYDAALMVEkJ_q40kejO7lsZBA')
    elif message.text.lower() == 'grinch':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAANdXrxInk7-yspRSmOIfNSC-BpjvwcAAqADAALMVEkJkqb7QCRGKJQZBA')

@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    bot.send_message(message.chat.id, 'ID of this sticker is: '+message.sticker.file_id)

bot.polling()