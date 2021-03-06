import telebot
from constant import token
from telebot import types
bot = telebot.TeleBot(token)

#Инлайн меню_1 уровень
inline_keyboard= types.InlineKeyboardMarkup(row_width=1)
btn_1= types.InlineKeyboardButton(text="Обновить", callback_data="1")
#btn_3= types.InlineKeyboardButton(text="Погода на завтра", callback_data="3")
#btn_4= types.InlineKeyboardButton(text="Погода на неделю", callback_data="4")
inline_keyboard.add(btn_1)
"""#Инлайн меню_2 уровень
inline_keyboard2= types.InlineKeyboardMarkup(row_width=1)
btn_1_2= types.InlineKeyboardButton(text="CRM", callback_data="CRM")
btn_3_2= types.InlineKeyboardButton(text="Бизнес процессы", callback_data="Bp")
btn_4_2= types.InlineKeyboardButton(text="Группы / Задачи", callback_data="groups")
btn_5_2= types.InlineKeyboardButton(text="CRM Маркетинг", callback_data="Marketing")
btn_6_2= types.InlineKeyboardButton(text="Обратно", callback_data="back")
inline_keyboard2.add(btn_1_2,btn_3_2,btn_4_2,btn_5_2,btn_6_2,)"""


@bot.message_handler(commands=['start'])
def hello_post(message):
    bot.send_message(message.chat.id, 'Сообщение о погоде', reply_markup=inline_keyboard)

@bot.callback_query_handler (func=lambda call: True)
def callback_inline(call):
    if call.data == "1":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= "Обновленная инфа о погоде", reply_markup=inline_keyboard)


bot.polling(none_stop=True)
