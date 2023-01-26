'''
Dictionary tg-bot with cats
'''
import random
from telebot import types, TeleBot
import dct


TOKEN = '5964923152:AAFJAz5RwOt9411U5TqFaPDuGoRzeQL5Rbg'
bot = TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def get_start(message):
    '''
    Обработчик команды старт
    '''
    welcome = open('cats/welcome3.webp', 'rb')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('словарь 📖')
    item2 = types.KeyboardButton('котофото😺')
    item3 = types.KeyboardButton('инфо❓')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,"Привет, {0.first_name}! Я помогу тебе разобраться в сложных (и не очень сложных) геодезических терминах 🌍📐".format(message.from_user), reply_markup = markup)
    bot.send_sticker(message.chat.id, welcome)


@bot.message_handler(content_types=["text", "audio", "document", "photo", "sticker", "video",
                 "video_note", "voice", "location", "contact", "new_chat_members",
                 "left_chat_member", "new_chat_title", "new_chat_photo",
                 "delete_chat_photo", "group_chat_created",
                 "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id",
                 "migrate_from_chat_id", "pinned_message", "animation"])
def bot_message(message):
    '''
    Обработчик сообщений
    '''
    cat_list = ['cat1.webp', 'cat2.webp', 'cat3.webp', 'cat4.webp', 'cat5.webp', 'cat6.webp', 'cat7.webp', 'cat8.webp', 'cat9.webp', 'cat10.webp']
    dont_know = ['Даже не знаю, что на это ответить🐾', 'Пока я не знаю этот термин🤷', 'Не знаю, что это. Знать все на свете нереально🐱']
    
    if message.chat.type == 'private':
        if message.content_type == 'text':
            word = message.text.lower()

            if word == 'словарь 📖':
                bot.send_message(message.chat.id, 'Введи термин, аббревиатуру или словосочетание, например, EFT или эллипсоид Красовского🌎')
            
            elif word in dct.DEFINITIONS:
                bot.send_message(message.chat.id, dct.DEFINITIONS[word])

            elif word in ['привет', 'ghbdtn', 'hi', 'hello', 'добрый день', 'доброе утро', 'добрый вечер']:
                bot.send_message(message.chat.id, "Привет-привет 👋, {0.first_name}!".format(message.from_user))

            elif word == 'котофото😺':
                photo = open('cats/' + random.choice(cat_list), 'rb')
                bot.send_photo(message.chat.id, photo)

            elif word == 'инфо❓':
                bot.send_message(message.chat.id, 'Котобот-словарик🐈 знает около 400 геодезических терминов и обладает портфолио из 10 фотографий. Если какого-то термина не нашлось в словаре, пиши ➡ @goodyrev')

            else:
                bot.send_message(message.chat.id, random.choice(dont_know))
                hz = open('cats/hz.webp', 'rb')
                bot.send_sticker(message.chat.id, hz)

        elif message.content_type == 'sticker':
            bot.send_message(message.chat.id, 'Классный стикер! Дай пять🐾')
            five = open('cats/five.webp', 'rb')
            bot.send_sticker(message.chat.id, five)

        elif message.content_type == 'animation':
            bot.send_message(message.chat.id, 'Прикольная гифка))')
            bot.send_message(message.chat.id, 'А это моя любимая😹😻')
            gif = open('cats/catt.gif', 'rb')
            bot.send_animation(message.chat.id, gif)
            
        else:
            bot.send_message(message.chat.id, 'Матерь котья, что это?🙀 Я такой тип данных не поддерживаю(')

bot.polling(none_stop=True)
