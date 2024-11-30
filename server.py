import socket

HOST = '0.0.0.0'  # Lắng nghe tất cả các kết nối
PORT = int(os.getenv("PORT", 12345))  # Heroku cung cấp PORT qua biến môi trường

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Server đang chạy trên {HOST}:{PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Kết nối từ {addr}")

        data = client_socket.recv(1024).decode('utf-8')
        print(f"Dữ liệu nhận được: {data}")
        client_socket.send(f"Server echo: {data}".encode('utf-8'))

        client_socket.close()

if __name__ == "__main__":
    start_server()
