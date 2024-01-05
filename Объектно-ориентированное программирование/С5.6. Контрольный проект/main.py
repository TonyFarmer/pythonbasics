import telebot
from extensions import * 
from config import TOKEN, available_symbols

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start", "help"])
def initial(message: telebot.types.Message):
    if message.text == "/start":
        bot.send_message(message.chat.id, "Привет!")
    bot.send_message(message.chat.id, "Пример того, как конвертировать валюту:\n\
                USD RUB 20 - пример перевода 20 долларов в рубли;\n\
                EUR USD 3.5 - пример перевода 3.5 евро в доллар") 

@bot.message_handler(commands=["values"])
def values(message: telebot.types.Message):
    bot.send_message(available_symbols[:409])
    bot.send_message(available_symbols[409:])

@bot.message_handler(content_types=["text"])
def pair_convertion(message: telebot.types.Message):
    text = message.text.split()
    try:
        if len(text) != 3:
            raise WrongFormat("Неправильный формат (смотри пример /help)")
        elif text[0] not in available_symbols:
            raise WrongSym("Неправильный начальный символ (доступные символы /values)")
        fsym, tsym, num = text
        sum = Convertion.get_price(fsym, tsym, num)
        bot.send_message(message.chat.id, f"{num} {fsym} = {sum} {tsym}")
    except UserError as e:
        bot.reply_to(message, f"Ошибка пользователя\n{e}")
    except RequestError as e:
        bot.reply_to(message, f"Ошибка на сервере\n{e}")


if __name__ == "__main__":
    bot.polling()