import select
from socket import AF_INET, SOCK_STREAM, socket, SOL_SOCKET, SO_REUSEADDR
import pickle
import logging

import log.server_log_config

logger = logging.getLogger('server')


class ServerSocket:

    def __init__(self):
        self.port = 7777
        self.soc = socket(AF_INET, SOCK_STREAM)
        self.clients = []
        logger.info(f'Инициализация сокета прошла успешна.')

    def read_requests(self, r_clients, all_clients):
        """ Чтение запросов из списка клиентов
        """
        responses = {}  # Словарь ответов сервера вида {сокет: запрос}

        for sock in r_clients:
            try:
                data = sock.recv(1024).decode('utf-8')
                responses[sock] = data
            except:
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                all_clients.remove(sock)

        return responses

    def write_responses(self, requests, w_clients, all_clients):
        """ Эхо-ответ сервера клиентам, от которых были запросы
        """

        for sock in w_clients:
            if sock in requests:
                try:
                    # Подготовить и отправить ответ сервера
                    resp = requests[sock].encode('utf-8')
                    # Эхо-ответ сделаем чуть непохожим на оригинал
                    logger.info(f'Ответ Клиенту {requests[sock]}.')
                    sock.send(resp.upper())
                except:  # Сокет недоступен, клиент отключился
                    print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                    sock.close()
                    all_clients.remove(sock)

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

    def server(self, ):
        logger.info(f'Тестовое подключения с участия сокета успешно.')
        self.soc.bind(('', self.port))
        self.soc.listen(5)
        self.soc.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        logger.info(f'Включаем settimeout для не блокировки сокета')
        self.soc.settimeout(0.1)
        while True:
            try:
                conn, addr = self.soc.accept()
                logger.error(f'Ожидания клиента accept')
            except OSError:
                logger.error(f'Ошибка ожидания')  # Знаю что тут бодет большой лог Играюсь
                pass
            else:
                self.clients.append(conn)
                logger.info(f'Получен запрос на соединение {addr}')
            finally:
                # Проверить наличие событий ввода-вывода
                wait = 2
                r = []
                w = []
                try:
                    r, w, e = select.select(self.clients, self.clients, [], wait)
                except:
                    pass  # Ничего не делать, если какой-то клиент отключился

                requests = self.read_requests(r, self.clients)  # Сохраним запросы клиентов
                if requests:
                    self.write_responses(requests, w, self.clients)  # Выполним отправку ответов клиентам

