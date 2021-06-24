from socket import AF_INET, SOCK_STREAM, socket, SOL_SOCKET, SO_REUSEADDR
import time
import pickle
import logging

import log.client_log_config
logger = logging.getLogger('client')


class ClientSocket:
    def __init__(self):
        self.port = 7777
        self.soc = socket(AF_INET, SOCK_STREAM)
        logger.info(f'Инициализация сокета прошла успешна.')

    def client(self, msg, name, password,param, test=''):
        logger.info(f'Начинается отправка сообщения на сервер.')
        if test != '':
            logger.info(f'Отправка сообщения на сервер прошла успешна')
            return 'Все OK'
        else:
            try:
                self.soc.connect(('localhost', self.port))
                if param == '2':
                    data = self.soc.recv(1024)
                    logger.info(f'Сообщение получено {pickle.loads(data)}')
                elif param == '1':
                    # message = {
                    #     'action': 'authenticate',
                    #     'time': time.time(),
                    #     'user': {'name': name,
                    #              'password': password},
                    #     'messages': msg}
                    message = {
                        'messages': msg}
                    try:
                        self.soc.send(pickle.dumps(message))
                    except pickle.PickleError:
                        logger.error('Не удалось сообщни серверу')
                    data = self.soc.recv(1024)
                    logger.info(f'Сообщение от сервера {pickle.loads(data)}')
                    self.soc.close()
                    logger.info(f'Сокет успешно закрыт')
                    return pickle.loads(data).get('respons')
                else:
                    self.soc.close()
                    logger.error(f'Аварийное закрытие')

            except ConnectionRefusedError:
                logger.critical('Ошибка соеденинения')
