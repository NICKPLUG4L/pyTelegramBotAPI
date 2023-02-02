#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

API_TOKEN = '<6154197736:AAF7eurdlRVSQrLz6amePZ8uk9uP029uxyo>'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
ciao, sono Stick, il bot più semplice di tutti che proverà a fare un pò di conversazione :)
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
   if message.text=='Ciao': 
    elif message.text=='ciao'
    elif message.text=='buongiorno'
    bot.reply_to(message, 'ciao sono stick, come va?')
   elif message.text=='come va'
 bot.reply_to(message, 'bene te?')
    elif message.text=='che fai nella vita?'
     bot.reply_to(message, 'niente,sono qui mi scrivo con la gente. te che fai nella vita?')
        elif message.text=='io lavoro'
        bot.reply_to(message, 'che lavoro fai?')
        elif message.text=='faccio il designer?'
        elif message.text=='sono un designer'
        elif message.text=='ho un bar'
        elif message.text=='lavoro in un bar'
        bot.reply_to(message, 'niente,sono qui mi scrivo con la gente. te che fai nella vita?')
        elif message.text=='io studio'
        elif message.text=='sono uno studente'
         bot.reply_to(message, 'che cosa studi?')
             elif message.text=='faccio un liceo'
                 elif message.text=='faccio il liceo scientifico scienze applicate'
                    elif message.text=='faccio un liceo'
                    bot.reply_to(message, 'che liceo?')
                    elif message.text=='liceo scienze applicate'
                            bot.reply_to(message, 'difficile?')
                            elif message.text=='non tanto'
                                elif message.text=='no'
                                    elif message.text=='si'
                                        elif message.text=='si abbastanza'
                                            elif message.text=='abbastanza'
                                                elif message.text=='molto'
                                                
                                               else:
                                                bot.reply_to(message, 'sono stato appena creato ci vediamo quando sapro scriverti di più, quando non sarò così stupido')
                                                
                    
        
        
        
    
    

bot.polling()
