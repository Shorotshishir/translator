import socket

HOST, PORT = "localhost", 5001


def helpDesk():
    print("HELP Details")
    helpset = [
        ['--h', 'help Menu'],
        ['q', 'quit']
    ]
    for helps in helpset:
        print(f'{helps[0]}\t{helps[1]}')


def main():
    """

    :rtype: object
    """
    HOST, PORT = "localhost", 5001
    while True:
        data = input("enter text: ")
        if data == 'q': break
        if data == '--h':
            helpDesk()
            continue
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

            # Connect to server and send data
            sock.connect((HOST, PORT))
            sock.sendall(bytes(data + "\n", "utf-8"))
            # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")

            # print("Sent:     {}".format(data))
            print(f'translated: {received}')


if __name__ == '__main__':
    main()
