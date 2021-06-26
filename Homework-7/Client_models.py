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

    def client(self, msg, name, password, param, test=''):
        logger.info(f'Начинается отправка сообщения на сервер.')

        try:
            self.soc.connect(('localhost', self.port))
            if param == '2':
                data = self.soc.recv(1024).decode('utf-8')
                print(data)
                logger.info(f'Сообщение получено {data}')
            elif param == '1':
                try:
                    self.soc.send(msg.encode('utf-8'))
                    logger.info(f'Сообщение отправлено {msg}')
                    data = self.soc.recv(1024).decode('utf-8')
                    print(data)
                    logger.info(f'Сообщение получено {data}')
                except pickle.PickleError:
                    logger.error('Не удалось сообщни серверу')
                # data = self.soc.recv(1024).decode('utf-8')
                # logger.info(f'Сообщение от сервера {data}')

                # return pickle.loads(data).get('respons')
            elif param == '3':
                self.soc.close()
                logger.info(f'Сокет успешно закрыт')

        except ConnectionRefusedError:
            logger.critical('Ошибка соеденинения')
