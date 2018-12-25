# Программа сервера для получения приветствия от клиента и отправки ответа
from socket import *
import time
import json

s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
s.bind(('', 8007))                # Присваивает порт 8007
s.listen(5)                       # Переходит в режим ожидания запросов;
                                  # Одновременно обслуживает не более
                                  # 5 запросов.
while True:
    buf = input()
    client, addr = s.accept()
    data = client.recv(1000000)
    print('Сообщение: ', data.decode('utf-8'), ', было отправлено клиентом: ', addr)
    msg = 'Привет, клиент'
    client.send(msg.encode('utf-8'))
    if buf == "exit":
        break
    client.close()
s.close()