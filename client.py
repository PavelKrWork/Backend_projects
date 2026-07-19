from socket import *

client = socket(AF_INET, SOCK_STREAM)

client.connect(('192.168.1.18', 8080))
data = client.recv(1024) # принимаем данные с сервера
msg = data.decode('utf-8')
print(f'server message: {msg}')

if msg == 'OK\n':
    print("Проверка успешна!")
else:
    print("Ошибка: сервер прислал неверные данные!")

client.close()
