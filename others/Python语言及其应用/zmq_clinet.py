import zmq

host = '127.0.0.1'
port = 6789
context = zmq.Context()
client = context.socket(zmq.REQ)
client.connect('tcp://%s:%s' % (host, port))
for i in range(6):
    request_str = input('---->')
    client.send_string(request_str )

    # reply_bytes = client.recv_json()
    # print(reply_bytes )
