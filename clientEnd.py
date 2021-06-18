from TranslatedData import TranslateData
import socket

HOST, PORT = "localhost", 5001


def helpDesk():
    print("HELP Details")
    helpset = [
        ['--h', '''\thelp Menu'''],
        ['set_dest:' , 
        '''to change the translated language, type set_dest:ja for japanese.
           \tfor all set_dest: keys check [API Documentation of googletrans]
           \t(https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages)'''],
        ['q', '''\tquit this client''']
    ]
    for helps in helpset:
        print(f'{helps[0]}\t{helps[1]}')


def main():
    """
    :rtype: object
    """
    HOST, PORT = "localhost", 5001
    d = TranslateData()
    d.dest='bn'
    while True:
        
        data = input("enter text: ")
        if data == 'q': break
        if data== '':
            continue
        if data == '--h':
            helpDesk()
            continue
        if data.startswith('set_dest:'):
            d.dest = data[11:]
            continue

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            d.txtdata = data
            sock.connect((HOST, PORT))
            sock.sendall(bytes(d.toJson() + "\n", "utf-8"))
            received = str(sock.recv(1024), "utf-8")
            print(f'translated: {received}')

if __name__ == '__main__':
    main()
