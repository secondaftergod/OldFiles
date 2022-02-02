import re
import telebot
import subprocess
import re
from stat_total import print_stat
from stat_total import telegram_shotdown
import time


bot = telebot.TeleBot('5012937098:AAHnwtBj4w3cn9f_yfCh_I5UCOurXzQ9r7M')

from telebot import types

# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text =='О' or re.findall(r'\w',message.text):
        #bot.send_message(message.from_user.id, "Hi")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()

        #key_balance_alesia = types.InlineKeyboardButton(text='Баланс Алеся', callback_data='bal_alesia')
        # И добавляем кнопку на экран
        #keyboard.add(key_balance_alesia)

        #key_total_in_alesia = types.InlineKeyboardButton(text='Ставка Алеся', callback_data='total_in_alesia')
        # И добавляем кнопку на экран
        #keyboard.add(key_total_in_alesia)

        #key_stattistic_alesia = types.InlineKeyboardButton(text='Статистика Алеся', callback_data='stat_alesia')
        #keyboard.add(key_stattistic_alesia)

        key_balance_ostap = types.InlineKeyboardButton(text='Баланс Остап', callback_data='bal_ostap')
        # И добавляем кнопку на экран
        keyboard.add(key_balance_ostap)

        key_total_in_ostap = types.InlineKeyboardButton(text='Ставка Остап', callback_data='total_in_ostap')
        # И добавляем кнопку на экран
        keyboard.add(key_total_in_ostap)

        key_stattistic_ostap = types.InlineKeyboardButton(text='Статистика Остап', callback_data='stat_ostap')
        keyboard.add(key_stattistic_ostap)

        key_shotdown = types.InlineKeyboardButton(text='Выключение Mac', callback_data='shotdown')
        # И добавляем кнопку на экран
        keyboard.add(key_shotdown)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='CHOOSE AND PRESS BUTTON', reply_markup=keyboard)

# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "bal_ostap":
        with open('money_ostap.txt', 'r') as file_in:
            msg = file_in.readline()
        bot.send_message(call.message.chat.id, msg)
        file_in.close()

    elif call.data == "total_in_ostap":
        with open('money_in_now_ostap.txt', 'r') as file_in:
            msg2 = file_in.readline()
        bot.send_message(call.message.chat.id, msg2)
        file_in.close()
    elif call.data == "stat_ostap":
        print_stat('ostap')
        with open('print_stat_ostap.txt', 'r') as file_in:
            for i in file_in:
                bot.send_message(call.message.chat.id, i.strip())
            file_in.close()
    #elif call.data == "bal_alesia":
        #with open('money_alesia.txt', 'r') as file_in:
            #msg = file_in.readline()
        #bot.send_message(call.message.chat.id, msg)
        #file_in.close()

    #elif call.data == "total_in_alesia":
        #with open('money_in_now_alesia.txt', 'r') as file_in:
            #msg2 = file_in.readline()
        #bot.send_message(call.message.chat.id, msg2)
        #file_in.close()
    #elif call.data == "stat_alesia":
        #print_stat('alesia')
        #with open('print_stat_alesia.txt', 'r') as file_in:
            #for i in file_in:
                #bot.send_message(call.message.chat.id, i.strip())
            #file_in.close()
    elif call.data=='shotdown':
        subprocess.call(['osascript', '-e', 'tell app "system events" to shut down'])
        msg1 = f'Power off'
        bot.send_message(call.message.chat.id, msg1)
        #while True:
            #money = telegram_shotdown()
            #if telegram_shotdown() > money:
                #subprocess.call(['osascript', '-e', 'tell app "system events" to shut down'])
                #msg1 = f'Power off, Total balance {money}'
                #bot.send_message(call.message.chat.id, msg1)





        # Отправляем текст в Телеграм

# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)