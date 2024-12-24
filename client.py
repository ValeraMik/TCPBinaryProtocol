import socket
import struct
import random

def start_client():
    host = '127.0.0.1'
    port = 65432

    # Створення TCP сокета
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Підключено до сервера {host}:{port}")

    for i in range(100):  # Надсилання 100 повідомлень
        # Генерація різнотипних повідомлень
        if i % 3 == 0:
            message = f"Text message {i}"
        elif i % 3 == 1:
            message = f"Number: {random.randint(1, 1000)}"
        else:
            message = f"Boolean: {random.choice([True, False])}"

        # Кодування повідомлення та формування заголовку довжини
        message_data = message.encode('utf-8')
        message_length = struct.pack('!I', len(message_data))
        client_socket.send(message_length + message_data)
        print(f"Відправлено: {message}")

        # Отримання відповіді від сервера
        header = client_socket.recv(4)
        if not header:
            break
        response_length = struct.unpack('!I', header)[0]
        response = client_socket.recv(response_length).decode('utf-8')
        print(f"Сервер: {response}")

    client_socket.close()
    print("З'єднання завершено.")

if __name__ == "__main__":
    start_client()
