import RPi.GPIO as gpio
import bluetooth as bt
import LED

def server():
    gpio.setmode(gpio.BCM)
    LED.setup(21, 'out')

    server_socket = bt.BluetoothSocket(bt.RFCOMM)
    server_socket.bind(('', 3))
    server_socket.listen(1)

    conn_socket, address = server_socket.accept()
    try:
        while True:
            data = conn_socket.recv(1024)
            data = str(data, 'utf-8')
            print(data)
            if data == 'turn on':
                print('receive "{}"'.format(data))
                LED.turnON(21)
            elif data == 'turn off':
                print('receive "{}"'.format(data))
                LED.turnOFF(21)

            send_data = input()
            conn_socket.send(send_data)
    finally:
        conn_socket.close()
        server_socket.close()
        gpio.cleanup()

if __name__ == '__main__':
    server()
