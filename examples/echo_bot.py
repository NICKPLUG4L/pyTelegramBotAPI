#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

API_TOKEN = '<6085802845:AAFzmaBLYBzoN20vtzR4KFoVzaZERo9XF34>'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
ciao, sono stiky
son stiky, un bot socievole con cui conversare!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    elif message.text== ciao'
    elif message.text==buongiorno'
    elif message.text==buona sera'
    elif message.text==salve'
    elif message.text==Ciao'
    elif message.text==buongiorno
    elif message.text==Buona sera'
    elif message.text==Salve'
    elif message.text==buonasera'
    elif message.text==Buonasera'
    bot.reply_to(message, ciao come ho già detto sono stilky oppure se per te è più facile puoi chiamarmi anche stiky!')
 elif message.text== come va?'
 elif message.text==come stai?'
    bot.reply_to(message, bene! te?')
     elif message.text==bene'
       bot.reply_to(message,sono felice per te')          
       elif message.text==ne bene ne male'
                  elif message.text==male'
                  elif message.text==Male'
                  elif message.text==malissimo'
                  elif message.text==Malissimo'
                      bot.reply_to(come mai?') 
                                  elif message.text==non mi è andata bene la giornta'
                                  elif message.text==non è andata bene la scuola'
                                  elif message.text==non è andata bene al lavoro'
                                  elif message.text==non è andata bene la giornata'
                                   bot.reply_to(message,cosa fai nella vita?')
                                               elif message.text==studio'
                                               elif message.text==Studio
                                               elif message.text==Sono uno studente
                                               elif message.text==sono unpo studente
                                                bot.reply_to(message, che cosa studi?')
                                                             elif message.text==frequento un liceo
                                                             elif message.text==frequento l università'
                                                             elif message.text==frequento il liceo scientifico scienze applicate
                                                             bot.reply_to(message,difficile?')
                                                                          elif message.text==si'
                                                                          elif message.text==si molto
                                                                          elif message.text==Si
                                                                          elif message.text==Si molto
                                                                          elif message.text==sì
                                                                          elif message.text==Sì
                                                                          elif message.text==Sì molto
                                                                          elif message.text==sì molto
                                                                          elif message.text==No 
                                                                          elif message.text==no
                                                                          elif message.text==abbastanza
                                                                          elif message.text==molto
                                                                          elif message.text==Abbastanza
                                                                          elif message.text==Molto
                                                                          elif message.text==Tanto
                                                                          elif message.text==tanto
                                                                          elif message.text==Neanche tanto
                                                                          elif message.text==neanche tanto
                                                                          
                                                                          if message.text==Lavoro
                                                                          if message.text==lavoro
                                                                          bot.reply_to(message,che lavoro fai?')
                                                                                      elif message.text==sono un designer 
                                                                                      elif message.text==Sono un designer 
                                                                                      elif message.text==disegno automobili
                                                                                      elif message.text==Disegno automobili
                                                                                      elif message.text==Ho un bar
                                                                                      elif message.text==ho un bar
                                                                                      elif message.text==lavoro in un bar
                                                                                      elif message.text==Lavoro in un bar
                                                                                      elif message.text==lavoro a un bar
                                                                                      elif message.text==Lavoro a un bar
                                                                                      else:
                                                                                           bot.reply_to(message,Sono appena stato creato, anche se non te l ho detto,se vuoi potrai riprovare a scrivermi tra un pò, quando sarò meno stupido! è stato bello scrivermi con te ci vediamo :)')
                                                                                       
                                                                                       
                                                                          
                                                                          
                                                                          
                                                                          
                                                                          
                                                             
                                                             
                                                
                                   
                                   
                                   
    
    

bot._polling()
