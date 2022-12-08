from flask import Flask
from flask import request
from flask import Response
from datetime import datetime
from telegram import *
from spreadsheet import append_range

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    msg = request.get_json()
    
    try:
        chat_id, message, sender_first_name = parse_message(msg)
        splited_message = message.split(' ')
    except Exception as error:
        send_message(chat_id, 'Ошибка сервера: {}'.format(error))

    if message == '/start':
        send_message(chat_id, "Чтобы добавить новую информацию о расходах, введи сообщение в следующем формате:\n\n[Название статьи расходов] [сумма]\n\n<b>Пример:</b> Обед в Канути 19")
    elif len(splited_message) < 2:
        send_message(chat_id, "Неверный формат входных данных. Команда **/start** покажет правильный формат")
    else:
        try:
            spending_name, cost = ' '.join(splited_message[:-1]), float(splited_message[-1])
            row = [spending_name, cost, sender_first_name, datetime.now().strftime("%d/%m/%Y %H:%M")]
            append_range(row)
            send_message(chat_id, f"<b>Добавил</b> 👍\nЧто-нибудь еще?")
        except:
            send_message(chat_id, "Неверный формат входных данных. Команда /start покажет правильный формат")

    return Response('ok', status=200)


if __name__ == '__main__':
    app.run(threaded=True)
