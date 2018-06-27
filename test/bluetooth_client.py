import bluetooth as bt

def client():
    port = 3
    client_socket = bt.BluetoothSocket(bt.RFCOMM)

    client_socket.connect(('AC:BC:32:B0:C6:E4', port))

    try:
        while True:
            send_data = input()
            client_socket.send(send_data)
            data = client_socket.recv(1024)
            print('received "{}"'.format(data))
    except:
        client_socket.close()

if __name__ == '__main__':
    client()
