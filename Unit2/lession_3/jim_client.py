# Программа клиента для отправки приветствия серверу и получения ответа

from socket import *
import json
import datetime,time
import argparse
import sys


def get_timestamp():
    dt = datetime.datetime.now()
    # value = datetime.datetime.fromtimestamp(time.mktime(dt.timetuple()))
    # print(value.strftime('%Y-%m-%d %H:%M:%S'))
    return (dt)

def create_conn():
    consol = argparse.ArgumentParser()
    consol.add_argument('addr',default='localhost')
    consol.add_argument('port',default=8007)
    return consol

presence_json = {
        "action": "presence",
        "time": get_timestamp(),
        "type": "status",
        "user": {
                "account_name":  "C0deMaver1ck",
                "status":      "Yep, I am here!"
        }
}

consol = create_conn()
parameters = consol.parse_args(sys.argv[1:])

while True:
    s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
    s.connect((parameters.addr, int(parameters.port)))   # Соединиться с сервером
    msg = presence_json
    s.send(json.dumps(msg).encode('utf-8'))
    data = s.recv(1000000)  # ответ от сервера
    print('Сообщение от сервера: ', data.decode('utf-8'), ', длиной ', len(data), ' байт')
    s.close()
