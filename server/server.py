from threading import Thread
import socket
from typing import List
import client

class Server(Thread):
    _soc: socket.socket = None
    clients: List[client.Client] = []

    def __init__(self):
        super(self)
        _soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _set_up(self):
        self._soc.bind('127.0.0.1', 8080)
        self._soc.listen()

    def run(self):
        while True:
            conn, addr = self._soc.accept()
            _client = client.Client(conn, addr, self)
            _client.start()
            self.clients.append(_client)
