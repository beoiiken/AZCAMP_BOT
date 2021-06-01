
import telebot
import constants
from sqldata import  SQLighter
from telebot import types
import datetime

bot = telebot.TeleBot(constants.token)
db=SQLighter('dbofazcamp.db')

global name
global surname
global phone


global ssat
global ssport
global stime
global sstyle
global sat
global sport
global time
global style
sat = False
sport = False
time = False
style = False

ssat = "*\n"
ssport = "*\n"
stime = "*\n"
sstyle = "*\n"








@bot.message_handler(commands=['start'])
def message_send(message):

    bot.send_message(message.chat.id, "Хэй! Добро пожаловать в онлайн-лагерь AZ Camp🥰 Я бот, который запишет вас на выбранные вами направления, и отправит вам ссылку на группы. Для выбора сфер, пожалуйста напишите /next ")


@bot.message_handler(commands=['next'])
def name_def(message):


        msg = bot.reply_to(message, "Напишите пожалуйста ваше имя ")
        bot.register_next_step_handler(msg, checkname_def)






def checkname_def(message):
    global name
    name=message.text
    if name.isalpha()==False:
        bot.send_message(message.chat.id, "Пожалуйста правильно заполните ваше имя")
        name_def(message)
    elif name==" ":
        bot.send_message(message.chat.id, "Пожалуйста правильно заполните ваше имя")
        name_def(message)
    else:
        surname_def(message)

def surname_def(message):
        msg = bot.reply_to(message, "Напишите пожалуйста ваше фамилию ")
        bot.register_next_step_handler(msg,checksur_def)

def checksur_def(message):
    global surname
    surname=message.text
    if surname.isalpha() == False:
        bot.send_message(message.chat.id, "Пожалуйста правильно заполните фамилию")
        surname_def(message)
    elif surname == " ":
        bot.send_message(message.chat.id, "Пожалуйста правильно заполните фамилию")
        surname_def(message)
    else:
        phone_def(message)
def phone_def(message):
    msg = bot.reply_to(message, "Напишите пожалуйста ваш номер телефона(примерное заполнение номера '87775039050')")
    bot.register_next_step_handler(msg, check_phone_def)
def check_phone_def(message):
    global phone

    phone=str(message.text)
    if phone.isdigit()==False:
        bot.send_message(message.chat.id, "Пожалуйста правильно заполните номер телефона")
        phone_def(message)
    elif  phone=="":

        bot.send_message(message.chat.id, "Пожалуйста правильно заполните номер телефона")
        phone_def(message)
    elif int(len(phone))<=10:
        bot.send_message(message.chat.id, "Пожалуйста правильно заполните номер телефона")
        phone_def(message)
    else:
        #rechoice


        global markup
        markup = types.InlineKeyboardMarkup(row_width=4)
        item1=types.InlineKeyboardButton("ПОСТУПЛЕНИЕ", callback_data="sat")
        item2 = types.InlineKeyboardButton("СПОРТ", callback_data="sport")
        item3 = types.InlineKeyboardButton("ТАЙМ-МЕНЕДЖМЕНТ", callback_data="1")
        item4 = types.InlineKeyboardButton("СТИЛЬ", callback_data="2")
        item6 = types.InlineKeyboardButton("Подтвердить", callback_data="Подтвердить")
        markup.add(item1,item2,item3,item4,item6)

        bot.send_message(message.chat.id, "Спасибо! Теперь можете выбирать направления.\n*Можете выбрать несколько")
        bot.send_message(message.chat.id,"Ваш выбор\n" + ssat + ssport + stime + sstyle, reply_markup=markup)
        bot.send_message(message.chat.id, "ВНИМАНИЕ!\n\nЕсли хотите отменить запись, вы можете снова нажать на кнопку запися.\n\nПосле нажатия кнопки 'Подтвердить', кнопки исчезают.\n\nВаши данные и записи на курсы автоматическим образом сохраняются в БД Azcamp.")





@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global sat
    global sport

    global time
    global style


    global ssat
    global ssport
    global stime
    global sstyle


    try:
        if call.message:
            if call.data=="sat":
                 if sat==False:
                     sat=True
                     ssat="Поступление\n"
                     bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                           text="Ваш выбор\n" + ssat + ssport + stime + sstyle, reply_markup=markup)
                 else:
                     sat=False
                     ssat="*\n"
                     bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                           text="Ваш выбор\n" + ssat + ssport + stime + sstyle, reply_markup=markup)

            elif call.data=="sport":
                if sport == False:
                    sport = True
                    ssport = "Спорт\n"
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="Ваш выбор\n" + ssat + ssport + stime + sstyle, reply_markup=markup)
                else:
                    sport= False
                    ssport = "*\n"
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="Ваш выбор\n" + ssat + ssport + stime + sstyle, reply_markup=markup)

            elif call.data == "1":
                if time == False:
                    time = True
                    stime= "Тайм-менеджмент\n"
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="Ваш выбор\n" + ssat + ssport + stime + sstyle, reply_markup=markup)
                else:
                    time= False
                    stime = "*\n"
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="Ваш выбор\n" + ssat + ssport + stime + sstyle, reply_markup=markup)

            elif call.data == "2":
                if style== False:
                    style= True
                    sstyle= "Стиль\n"
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="Ваш выбор\n" + ssat + ssport + stime + sstyle, reply_markup=markup)
                else:
                    style = False
                    sstyle = "*\n"
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="Ваш выбор\n" + ssat + ssport + stime + sstyle, reply_markup=markup)


            elif call.data == "Подтвердить":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Ваш выбор:\n" + ssat + ssport + stime + sstyle, reply_markup=None)


                if sat == True:
                     bot.send_message(call.message.chat.id, " https://t.me/joinchat/AAAAAFOHcdjLsaJYX_wTug\n- поступление ")
                if sport == True:
                     bot.send_message(call.message.chat.id, "https://t.me/joinchat/AAAAAEXfwiEDu6GfncPhvw n- спорт")
                if time == True:
                     bot.send_message(call.message.chat.id, "https://t.me/joinchat/AAAAAEihPnguSrZd261iMw \n- тайм-менеджмент")
                if style == True:
                     bot.send_message(call.message.chat.id, "https://t.me/joinchat/AAAAAFWRJ4XZAamzeA2k_g \n- стиль")
                bot.send_message(call.message.chat.id,"Ваш выбор был записан. Спасибо. Ниже можете увидеть ссылки. Переходите по ним, и становитесь лучшей версией себя!\n -С верой в Вас, AZ bot!")


                bot.send_message(610940864,"\nName - "+name+"\nSurname - "+surname+ "\nPhone -"+phone+"\nSat - "+str(sat)+"\nSport - "+str(sport)+"\nTime- "+str(time)+"\nStyle - "+str(style))
                db.add_sub(call.message.from_user.id, name, surname, phone, sat, sport, time, style)
                sat=False
                sport=False
                time=False
                style=False

                ssat = "*\n"
                ssport = "*\n"
                stime = "*\n"
                sstyle = "*\n"




    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True)


