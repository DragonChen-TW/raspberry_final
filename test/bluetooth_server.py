import bluetooth as bt

def server():
    server_socket = bt.BluetoothSocket(bt.RFCOMM)
    server_socket.bind(('', 3))
    server_socket.listen(1)

    conn_socket, address = server_socket.accept()
    try:
        while True:
            data = conn_socket.recv(1024)
            data = str(data, 'utf-8')
            print(data)

            send_data = input()
            conn_socket.send(send_data)
    finally:
        conn_socket.close()
        server_socket.close()

if __name__ == '__main__':
    server()
