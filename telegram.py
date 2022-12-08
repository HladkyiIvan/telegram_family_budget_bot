import requests
from config import BOT_TOKEN

def parse_message(message):
    print("message-->", message)
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    sender_first_name = message['message']['from']['first_name']
    return chat_id, txt, sender_first_name
 

def send_message(chat_id, message):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
                'chat_id': chat_id,
                'text': message,
                'parse_mode': 'html'
                }
   
    r = requests.post(url,json=payload)
    return r