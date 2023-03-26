import socket
import ssl
from bs4 import BeautifulSoup

HOST1 = 'www.its.ac.id'
HOST2 = 'classroom.its.ac.id'
PORT = 443

def getItems(container):
    soup = BeautifulSoup(container, 'html.parser')
    nav = soup.nav.ul
    items = []

    try:
        lis = nav.find_all('li')
        for li in lis:
            a = li.find('a')
            if a:
                items.append(a.text.strip())
            div = li.find('div')
            lis_a = div.find_all('a')
            for li_a in lis_a:
                items.append('\t' + li_a.text.strip())
    except AttributeError:
        pass
    return "\n".join(items)

def http_get(HOST, PORT):
    server_address = (HOST, PORT)
    request_header = b"GET / HTTP/1.1\r\nHost: " + HOST.encode() + b"\r\n\r\n"

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ssl_context = ssl.create_default_context()
    ssl_socket = ssl_context.wrap_socket(client_socket, server_hostname=HOST)
    ssl_socket.connect((server_address))

    ssl_socket.send(request_header)

    response = ''
    while True:
        received = ssl_socket.recv(1024)
        if not received:
            break
        response += received.decode('utf-8')

    ssl_socket.close()
    header, body = response.split('\r\n\r\n', 1)

    return header, body


# Nomor 1-3
header1, body1 = http_get(HOST1, PORT)

# Nomor 4-5
header2, body2 = http_get(HOST2, PORT)



# Soal
questions = ["Cetaklah status code dan deskripsinya dari HTTP response header pada halaman its.ac.id",
        "Cetaklah versi Content-Encoding dari HTTP response header di halaman web its.ac.id",
        "Cetaklah versi HTTP dari HTTP response header pada halaman web its.ac.id",
        "Cetaklah property charset pada Content-Type dari HTTP response header pada halaman classroom.its.ac.id",
        "Dapatkanlah daftar menu pada halaman utama classroom.its.ac.id dengan melakukan parsing HTML"]

# Jawaban
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

answers.append(getItems(body2))

# Print
for index, (q, a) in enumerate(zip(questions, answers)):
    print("Nomor %d: %s" % (index+1, q))
    print("Jawaban:\n%s\n" %(a))





