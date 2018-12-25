# Программа клиента для отправки приветствия серверу и получения ответа
from socket import *
while True:
    s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
    s.connect(('localhost', 8007))   # Соединиться с сервером
    msg = 'Привет, сервер'
    s.send(msg.encode('utf-8'))
    data = s.recv(1000000)
    print('Сообщение от сервера: ', data.decode('utf-8'), ', длиной ', len(data), ' байт')
    s.close()