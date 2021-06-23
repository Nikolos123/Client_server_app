from socket import AF_INET, SOCK_STREAM, socket, SOL_SOCKET, SO_REUSEADDR
import pickle
import logging

import log.server_log_config

logger = logging.getLogger('server')


class ServerSocket:

    def __init__(self):
        self.port = 7777
        self.soc = socket(AF_INET, SOCK_STREAM)
        self.client = []
        logger.info(f'Инициализация сокета прошла успешна.')

    @classmethod
    def kwargs(self, colections):

        if colections.get('user').get('name') == 'Nikolay' and colections.get('user').get('password') == '1111':
            ans = {
                'code': 200,
                'user': colections.get('user').get('name')
            }
            logger.info(f'Код ответа 200 Авторизация успешна.')
        else:
            ans = {
                'code': 401,
                'user': colections.get('user').get('name')
            }
            logger.error(f'Код ответа 401 Авторизация не пройдена.')
        return ans

    def server(self, test=False):

        if test:
            logger.info(f'Тестовое подключения без участия сокета успешно.')
            return test

        else:
            logger.info(f'Тестовое подключения с участия сокета успешно.')
            self.soc.bind(('', self.port))
            self.soc.listen(5)
            self.soc.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            logger.info(f'Включаем settimeout для не блокировки сокета')
            self.soc.settimeout(0.1)
            while True:
                try:
                    client, addr = self.soc.accept()
                    logger.error(f'Ожидания клиента accept')
                except OSError:
                    logger.error(f'Ошибка ожидания')  # Знаю что тут бодет большой лог Играюсь
                    client = ''
                    pass
                else:
                    self.client.append(client)
                    logger.info(f'Получен запрос на соединение {addr}')
                if client:
                    data = client.recv(1024)
                    ans = self.kwargs(pickle.loads(data))

                    if ans.get('code') == 200:
                        respons = {
                            'respons': 200,
                            'message': f'Авторизация прошла успешная.Добро пожаловать в чат {ans.get("user")} '
                        }
                        logger.info(f'Ответ сервера {respons}')
                    else:
                        respons = {
                            'respons': ans.get('code'),
                            'message': f'Ошибка авторизации пользователя {ans.get("user")} в базе не существует '
                        }
                        logger.info(f'Ответ сервера {respons}')
                    client.send(pickle.dumps(respons))
                    logger.info(f'Произошла упаковка данных и отправка данных на клиент')
                    client.close()
                    logger.info(f'Сессия закрыта')
