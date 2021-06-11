from socket import AF_INET, SOCK_STREAM, socket, SOL_SOCKET, SO_REUSEADDR
import time
import pickle


class ClientSocket:

    def __init__(self):
        self.port = 7777
        self.soc = socket(AF_INET, SOCK_STREAM)

    def client(self, msg, name, password, test=''):
        if test != '':
            return 'Все OK'
        else:
            self.soc.connect(('localhost', self.port))
            message = {
                'action': 'authenticate',
                'time': time.time(),
                'user': {'name': name,
                         'password': password},
                'messages': msg}
            self.soc.send(pickle.dumps(message))
            data = self.soc.recv(1024)
            print('Сообщение от сервера', pickle.loads(data))
            self.soc.close()
