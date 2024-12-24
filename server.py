import socket
import struct

def start_server():
    host = '127.0.0.1'
    port = 65432

    # Створення TCP сокета
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Сервер запущено на {host}:{port}")

    client_socket, client_address = server_socket.accept()
    print(f"З'єднання встановлено з {client_address}")

    for _ in range(100):  # Очікування 100 повідомлень
        # Отримання заголовку (4 байти для довжини)
        header = client_socket.recv(4)
        if not header:
            break
        message_length = struct.unpack('!I', header)[0]

        # Отримання повідомлення на основі довжини
        message = client_socket.recv(message_length).decode('utf-8')
        print(f"Клієнт: {message}")

        # Надсилаємо відповідь
        response = f"Сервер отримав: {message}"
        response_data = response.encode('utf-8')
        response_length = struct.pack('!I', len(response_data))  # Заголовок довжини
        client_socket.send(response_length + response_data)

    client_socket.close()
    server_socket.close()
    print("З'єднання завершено.")

if __name__ == "__main__":
    start_server()
