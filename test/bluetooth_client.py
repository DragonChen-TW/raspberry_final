import bluetooth as bt

def client():
    port = 3
    client_socket = bt.BluetoothSocket(bt.RFCOMM)

    client_socket.connect(('B8:27:EB:C2:41:0D', port))

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
