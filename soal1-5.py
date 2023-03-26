import socket
import ssl

HOST1 = 'www.its.ac.id'
HOST2 = 'classroom.its.ac.id'
PORT = 443


# Nomor 1-3
server_address = (HOST1, PORT)
request_header = b"GET / HTTP/1.1\r\nHost: " + HOST1.encode() + b"\r\n\r\n"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ssl_context = ssl.create_default_context()
ssl_socket = ssl_context.wrap_socket(client_socket, server_hostname=HOST1)
ssl_socket.connect((server_address))

ssl_socket.send(request_header)

response1 = ''
while True:
    received = ssl_socket.recv(1024)
    if not received:
        break
    response1 += received.decode('utf-8')

ssl_socket.close()
header1, body1 = response1.split('\r\n\r\n', 1)

# Nomor 4-5
server_address = (HOST2, PORT)
request_header = b"GET / HTTP/1.1\r\nHost: " + HOST2.encode() + b"\r\n\r\n"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ssl_context = ssl.create_default_context()
ssl_socket = ssl_context.wrap_socket(client_socket, server_hostname=HOST2)
ssl_socket.connect((server_address))

ssl_socket.send(request_header)

response2 = ''
while True:
    received = ssl_socket.recv(1024)
    if not received:
        break
    response2 += received.decode('utf-8')

ssl_socket.close()
header2, body2 = response2.split('\r\n\r\n', 1)


questions = ["Cetaklah status code dan deskripsinya dari HTTP response header pada halaman its.ac.id",
        "Cetaklah versi Content-Encoding dari HTTP response header di halaman web its.ac.id",
        "Cetaklah versi HTTP dari HTTP response header pada halaman web its.ac.id",
        "Cetaklah property charset pada Content-Type dari HTTP response header pada halaman classroom.its.ac.id",
        "Dapatkanlah daftar menu pada halaman utama classroom.its.ac.id dengan melakukan parsing HTML"]

answers = []

answers.append(" ".join(header1.split("\n")[0].split(" ")[1:]))
if 'content-encoding' in header1.lower():
    for header in header1.split('\r\n'):
        if header.startswith('Content-Encoding'):
            answers.append(header.split(" ")[1])
else:
    answers.append("Content-Encodding is not found")
answers.append(header1.split("\n")[0].split(" ")[0])
if 'content-type' in header2.lower():
    for header in header2.split('\r\n'):
        if header.startswith('Content-Type'):
            if 'charset' in header.lower():
                for content_type in header.split(" "):
                    if content_type.startswith('charset'):
                        answers.append(content_type.split("=")[1])
else:
    answers.append("Content-Type is not found")

answers.append("Belum Ada")
# answers = [" ".join(header1.split("\n")[0].split(" ")[1:]),
#         "Belum Ada",
#         header1.split("\n")[0].split(" ")[0],
#         " ".join(header2.split("\n")[3].split(" ")[1:]),
#         "Belum Ada"]
# Jawaban
for index, (q, a) in enumerate(zip(questions, answers)):
    print("Nomor %d: %s" % (index+1, q))
    print("Jawaban: %s" %(a))

print("=====HEADER 1=====")
print(header1)
print("=====HEADER 2=====")
print(header2)

# nomor1 = response.split("\n")[0].split(" ")
# print("Answer:",nomor1[1],nomor1[2],"\n")




