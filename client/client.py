import socket
from common.types import CONN_INFO, DICT
import server
from threading import Thread
import pickle
import time

class Client(Thread):
    _client: socket.socket = None
    _info: CONN_INFO = None
    _server: server.Server= None

    def __init__(
        self, con: socket.socket, info: CONN_INFO, server: server.Server):
        super(self)
        self._client = con
        self._info = info
        self._server = server

    def send(self, data: DICT):
        raw_data = pickle.dumps(data)
        self._client.sendall(raw_data)

    def run(self):
        for i in range(0, 10):
            self.send(f'Hello from server {i+1}')
            time.sleep(1)
        self._client.close()