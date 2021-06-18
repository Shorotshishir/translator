from TranslatedData import TranslateData
from googletrans import Translator

import json
import socketserver
from types import SimpleNamespace

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        data = TranslateData()
        data= json.loads(str(self.data,'utf-8'), object_hook=lambda d: SimpleNamespace(**d))
        translator = Translator()
        translated = translator.translate(text=data.txtdata, dest=data.dest)
        self.data = translated.text
        print(self.data)
        self.request.sendall(str.encode(self.data, 'utf-8'))

if __name__ == "__main__":
    HOST, PORT = "localhost", 5001

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()

