#-*-coding:utf8;-*-
#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# encoding: utf-8
import re, sys, time, json, threading, base64, traceback,time, random, datetime, androidhelper
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from telepot.namedtuple import InlineKeyboardMarkup, ReplyKeyboardMarkup
from telepot.namedtuple import InlineQueryResultArticle, InputTextMessageContent
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent

######### Modulos ###########
import telepot, sys, os, sys, random, urllib, urllib2, json, platform
from functools import partial
from telepot.namedtuple import InlineQueryResultArticle
from datetime import datetime
import threading, time, datetime, string
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent
from pprint import pprint
import string
############ UTF8 ########
os.system("clear")
reload(sys)

droid = androidhelper.Android()
## BOT Config
today = datetime.datetime.today()
t = today.strftime("[%H:%M:]")
tm= today.strftime("%H:%M:")
uptime = datetime.datetime.today()
hora = uptime.strftime("%H:%M")
data = uptime.strftime("%d/%m/%Y")
M = uptime.strftime("%m")
D = uptime.strftime("%d")
A = uptime.strftime("%Y")

bot =telepot.Bot('357538469:AAFGt5w4RRvX_UHCd7q-AenwYaioRdq-sNE')
NomeBot = 'ha'
  
message_with_inline_keyboard = None
message_with_inline_keyboar= None
message_with_inline_keyboardi = None
message_with_inline_keyboard = None

def on_chat_message(msg):
    usr = '@' + msg['from']['username']
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == "new_chat_member":
        if (chat_id == -1001112510856):
            bot.sendMessage(chat_id,'Bem vindo ao grupo , %s!' % (usr), reply_to_message_id=True)
        

    ### BOT PARAMTS
    
    contar = msg['message_id']
    send = bot.sendMessage
    reply_to_message_id= msg['from']['id']
    chat_id = msg['chat']['id']
    chat_type = msg['chat']['type']
    msg_id = msg['message_id']
    chat_type = msg['chat']['type']
    from_id = msg['from']['id']
    from_first_name = msg['from']['first_name']
    from_username = "@" + msg['from']['username']
    texto = msg['text']
    txt = msg['text'].split(' ')
    message = msg['text'].split()
    len_msg = len(message)
    
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat:', content_type, chat_type, chat_id)
    texto = msg['text']
    user = msg['from']['username']
    nome = msg['from']['first_name']
    id = msg['from']['id']
    
    send = bot.sendMessage
    chat_id = msg['chat']['id']
    reply_msg = "reply_to_message_id=msg['message_id']"
    txt = msg['text'].split(' ')
    message = msg['text'].split()
    len_msg = len(message)
    
    print(from_username)
    print("comando: " + texto)
    print(msg)
    txt = msg['text'].split(' ')

     # end
    if content_type != 'text':

        return


    command = msg['text'][-1:].lower()
    
##################
    if '/start' in texto or '#start' in texto or '/comecar' in texto or '/on' in texto:
       mark = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Regras 📄 ', callback_data='menus')]+[InlineKeyboardButton(text='Horários 🕐', callback_data='horarios')]])
       bot.sendMessage(chat_id, '''Olá, *{}*! Prazer em conhecê-lo
Quer ser divulgado primeiro veja as regras no botão abaixo ou quer saber os horários das divulgação olha nos botão abaixo também =]'''.format(msg['from']['first_name']), parse_mode='Markdown', reply_markup=mark)
   
         

 ######## Comandos Call######
 
 
def on_callback_query(msg):
    
    pprint(msg)
    query_id, from_id, data = telepot.glance(msg, flavor='callback_query')
    print('Query executado')
    print('''
nome: {} 
id: {}
query: {}
'''.format(msg['from']['first_name'], from_id, data))
  

    if data == 'menus':
       bot.sendMessage(from_id, '''*Regras 📃

1⃣ O canal não pode ter qualquer conteúdo adulto, violência, Pedofilia 

2⃣ Canal deve ter no mínimo 100 membros pra participar da lista 

3⃣ O canal deve estar sempre postando conteúdo 

⚠️ Nos iremos verificar o canal antes de adicionar em nossa lista*''', parse_mode='Markdown')

    elif data == 'horarios':
        bot.sendMessage(from_id, '''*➜ Horários 🕐

➜ Sábado e Domingo 📣
9:h a 11:h 

➜ Segunda a Sexta 📣
12:h a 20:h 
➜ ⚠️ Nota:  que eu de segunda a sexta e pouco mais tarde porque eu estudo no período de manhã*''', parse_mode='Markdown')
    else:
        bot.answerCallbackQuery(query_id, text='erro')
   
def on_inline_query(msg):
 
      
      
    def compute():

        query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')

        print('%s: Computing for: %s' % (threading.current_thread().name, query_string))


        articles = [InlineQueryResultArticle(

                        id='abcde', title='Telegram', input_message_content=InputTextMessageContent(message_text='Telegram is a messaging app')),dict(type='article',id='fghij', title='Google', input_message_content=dict(message_text='Google is a search engine'))]

        photo1_url = 'https://core.telegram.org/file/811140934/1/tbDSLHSaijc/fdcc7b6d5fb3354adf'

        photo2_url = 'https://www.telegram.org/img/t_logo.png'

        photos = [InlineQueryResultPhoto(

                    id='12345', photo_url=photo1_url, thumb_url=photo1_url),dict(type='photo',id='67890', photo_url=photo2_url, thumb_url=photo2_url)]


        result_type = query_string[-1:].lower()


        if result_type == 'a':

            return articles

        elif result_type == 'p':

            return photos

        else:

            results = articles if random.randint(0,1) else photos

            if result_type == 'b':

                return dict(results=results, switch_pm_text='Back to Bot', switch_pm_parameter='Optional start parameter')

            else:

                return dict(results=results)


    answerer.answer(msg, compute)



def on_chosen_inline_result(msg):

    result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')

    print('Chosen Inline Result:', result_id, from_id, query_string)
 




answerer = telepot.helper.Answerer(bot)



print('Ok! ligado.')   
bot.message_loop({'chat': on_chat_message,'callback_query': on_callback_query,'inline_query': on_inline_query,'chosen_inline_result': on_chosen_inline_result})
      
# Keep the program running.
# Keep the program running.

while 1:
    time.sleep(10)
   
