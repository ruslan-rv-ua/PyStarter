# pip install pytelegrambotapi


import zipfile
from datetime import datetime
from io import BytesIO

import requests
import telebot
from tabulate import tabulate

PB_API_URL = "https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11"
BOT_TOKEN = "7079500117:AAG0piBqaC62hQ8Q0GqE3NF19gi1Liarg84"
# t.me/pystarter_demo_bot

bot = telebot.TeleBot(BOT_TOKEN)


def get_currency_rates() -> dict:
    response = requests.get(PB_API_URL)
    return response.json()


def zip_rates(rates: dict, file_name: str) -> BytesIO:
    table = tabulate(rates, headers="keys")
    memory_zip = BytesIO()
    with zipfile.ZipFile(memory_zip, "w", zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.writestr(f"{file_name}.txt", table)
    memory_zip.seek(0)
    return memory_zip


@bot.message_handler(content_types=["text"])
def send_zip_to_telegram(message):
    print("Sending rates to telegram...")
    rates = get_currency_rates()
    file_name = f"{datetime.now():%Y-%m-%d_%H-%M-%S}"
    zip_file = zip_rates(rates, file_name)
    send_zip_to_telegram(zip_file)
    bot.send_message(message.chat.id, message.text)
    # bot.send_document(message.chat.id, zip_file)
    print("Done")


if __name__ == "__main__":
    print("Starting bot...")
    # bot.infinity_polling()
    bot.polling()
