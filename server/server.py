import socket
import configparser

# Baca file konfigurasi
config = configparser.ConfigParser()
config.read('config.conf')

# Dapatkan nilai port dari file konfigurasi
port = int(config['SERVER']['PORT'])

# Buat socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket ke alamat dan port yang diberikan
server_address = ('', port)
sock.bind(server_address)

# Listen untuk koneksi masuk
sock.listen(1)

while True:
    # Tunggu koneksi masuk
    connection, client_address = sock.accept()

    try:
        # Baca data dari koneksi
        data = connection.recv(1024)
        print(f"Received data: {data}")

        # Kirim balasan ke koneksi
        message = "Hello from the server"
        connection.sendall(message.encode())

    finally:
        # Tutup koneksi
        connection.close()
