from socket import *
import threading

def client_process(user, address):
    user.send('OK\n'.encode('utf-8'))
    user.close()

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(('0.0.0.0', 8080))
server.listen(5)

while True:
    user, addr = server.accept() # блокирующая функция
    print(f"Сервер поймал подключение от {addr}")

    client_thread = threading.Thread(target=client_process, args=(user, addr))

    client_thread.start()
