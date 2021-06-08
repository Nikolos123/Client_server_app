from socket import AF_INET, SOCK_STREAM, socket, SOL_SOCKET, SO_REUSEADDR
import time
import pickle


class ClientServerSocket:

    def __init__(self):
        self.port = 7777
        self.soc = socket(AF_INET, SOCK_STREAM)

    @classmethod
    def kwargs(self, colections):

        if colections.get('user').get('name') == 'Nikolay' and colections.get('user').get('password') == '1111':
            ans = {
                'code': 200,
                'user': colections.get('user').get('name')
            }
        else:
            ans = {
                'code': 401,
                'user': colections.get('user').get('name')
            }
        return ans

    def server(self, test=''):
        if test != '':
            print('Все ОК')
        else:
            self.soc.bind(('', self.port))
            self.soc.listen(5)
            self.soc.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            # self.soc.setblocking(0.1)
            while True:
                self.soc.settimeout(0.1)
                try:
                    client, addr = self.soc.accept()

                    data = client.recv(1024)
                    ans = self.kwargs(pickle.loads(data))

                    if ans.get('code') == 200:
                        respons = {
                            'respons': 200,
                            'message': f'Авторизация прошла успешная.Добро пожаловать в чат {ans.get("user")} '
                        }
                    else:
                        respons = {
                            'respons': ans.get('code'),
                            'message': f'Ошибка авторизации пользователя {ans.get("user")} в базе не существует '
                        }

                    client.send(pickle.dumps(respons))
                    client.close()
                except OSError as ans:
                    print(ans)

    def client(self, msg, name, password,test=''):
        if test != '':
            print('Все OK')
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
