import errno
import threading
import time
import socket

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
body = '''Hello ,world! <h1> form </h1> {thread_name}'''

response_params = {
    'HTTP/1.0 200 OK',
    'Date: Sun,27 may 2018 01:01:01 GMT',
    'Content-Type: text/plain; charset=utf-8',
    'Content-Length: {}\r\n'.format(len(body.encode())),
    body,
}

response = "\r\n".join(response_params)


def handle_connection(conn, _):
    request = b""
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024)

    print(request)
    current_thread = threading.currentThread()
    content_length = len(body.format(thread_name=current_thread.name).encode())

    conn.send(response.format(thread_name=current_thread.name, length=content_length).encode())  # response 转为bytes后传输
    conn.close()


if __name__ == '__main__':
    # socket.AF_INET  服务器与服务器之间的网络通信
    # socket.SOCK_STREAM    基于TCP的流式SOCKET通信

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 端口复用
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind(('127.0.0.1', 8000))
    serversocket.listen(5)
    print("http://127.0.0.1:8000")
    try:
        while True:
            conn, addr = serversocket.accept()
            handle_connection(conn, addr)
    finally:
        print(1)
        serversocket.close()
