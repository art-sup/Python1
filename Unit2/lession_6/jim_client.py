# Программа клиента для отправки приветствия серверу и получения ответа

from socket import *
import json
import datetime, time
import argparse
import sys
from client_log_config import *
from decor import *

@decoration_log
def get_timestamp():
    dt = time.time()
    # value = datetime.datetime.fromtimestamp(time.mktime(dt.timetuple()))
    # print(value.strftime('%Y-%m-%d %H:%M:%S'))
    logger.debug("called function get_timestamp")
    return (dt)

@decoration_log
def create_conn():
    consol = argparse.ArgumentParser()
    consol.add_argument('--addr', default='localhost')
    consol.add_argument('--port', default=8007, type=int)
    logger.debug("called function create_conn")
    return consol


presence_json = {
    "action": "presence",
    "time": get_timestamp(),
    "type": "status",
    "user": {
        "account_name": "C0deMaver1ck",
        "status": "Yep, I am here!"
    }
}

consol = create_conn()
parameters = consol.parse_args(sys.argv[1:])

logger.info("------starting client--------")

while True:
    try:
        s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
        s.connect((parameters.addr, int(parameters.port)))  # Соединиться с сервером

    except s.error:
        logger.error('Caught exception socket.error : ' + s)
        logger.info("client not start")
    # s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
    # s.connect((parameters.addr, int(parameters.port)))  # Соединиться с сервером
    msg = presence_json
    s.send(json.dumps(msg).encode('utf-8'))
    data = s.recv(1000000)  # ответ от сервера
    # print('Сообщение от сервера: ', data.decode('utf-8'), ', длиной ', len(data), ' байт')
    logger.info('Сообщение от сервера: ' + data.decode('utf-8') + ' длиной ' + str(len(data)) + ' байт')
    s.close()
