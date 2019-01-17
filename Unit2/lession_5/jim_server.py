# Программа сервера для получения приветствия от клиента и отправки ответа
from socket import *
import time
import json
import sys
import argparse
from server_log_config import *


def create_conn():
    consol = argparse.ArgumentParser()
    consol.add_argument('-a', '--addr', default='')
    consol.add_argument('-p', '--port', default=8007)
    return consol


consol = create_conn()
parameters = consol.parse_args(sys.argv[1:])

s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
s.bind((parameters.addr, parameters.port))  # Присваивает порт 8007
s.listen(5)  # Переходит в режим ожидания запросов;
# Одновременно обслуживает не более
# 5 запросов.
logger.info("---------------Server waked up-----------------")

while True:
    client, addr = s.accept()
    data = client.recv(1000000)
    clientMessage = json.loads(data)
    if clientMessage['action'] == 'presence':
        # print('Сообщение: ', clientMessage['user']['status'], ', было отправлено клиентом: ', addr)
        logger.info('Сообщение: ' + clientMessage['user']['status'] + ' было отправлено клиентом: ' + str(addr))
        serverMessage = 'Сообщение получено'
    else:

        serverMessage = 'Ошибка при обработке presence - сообщения'
    client.send(serverMessage.encode('utf-8'))
    client.close()
