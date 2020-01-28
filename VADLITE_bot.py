import telebot
from telebot import types

bot = telebot.TeleBot('986672145:AAG5Mud3OyeNV21CppdHikwZkWRmSUI4mN4')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'йоу')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '/start - start\n /help - help\n /mars - mars')


players = [['Алекс', 0], ['Пух', 0], ['Рост', 0],
           ['Самарин', 0], ['Бочаров', 0], ['Ширай', 0],
           ['Митяй', 0], ['Мася', 0], ['Артюх', 0]]


def alex(pts):
    players[0][1] += float(pts)


def puh(pts):
    players[1][1] += float(pts)


def rost(pts):
    players[2][1] += float(pts)


def samarin(pts):
    players[3][1] += float(pts)


def bocharov(pts):
    players[4][1] += float(pts)


def shiray(pts):
    players[5][1] += float(pts)


def mityay(pts):
    players[6][1] += float(pts)


def mausya(pts):
    players[7][1] += float(pts)


def artyuh(pts):
    players[8][1] += float(pts)


@bot.message_handler(commands=['mars'])
def mars1(message):
    markup1 = types.InlineKeyboardMarkup(row_width=5)
    q1_a1 = types.InlineKeyboardButton('это не моя работа', callback_data='0 def')
    q1_a2 = types.InlineKeyboardButton('иногда включаюсь', callback_data='1 def')
    q1_a3 = types.InlineKeyboardButton('постоянно отрабатываю', callback_data='2 def')
    q1_a4 = types.InlineKeyboardButton('ломаю ноги', callback_data='3 def')
    markup1.row(q1_a1)
    markup1.row(q1_a2)
    markup1.row(q1_a3)
    markup1.row(q1_a4)
    bot.send_message(message.chat.id, 'Как ты играешь в защите?', reply_markup=markup1)


@bot.callback_query_handler(func=lambda call: True)
def first_question(call):
    if call.data == '0 def':
        alex(5)
        mausya(5)
    if call.data == '1 def':
        samarin(5)
        shiray(5)
    if call.data == '2 def':
        bocharov(5)
        rost(5)
        mityay(5)
    if call.data == '3 def':
        puh(5)
        artyuh(5)


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == 'йоу':
        bot.send_message(message.chat.id, 'йоу')
    elif message.text.lower() == 'yo':
        bot.send_message(message.chat.id, 'йоу')
    if message.text.lower() == 'хрю':
        bot.send_message(message.chat.id, '??')


bot.polling()