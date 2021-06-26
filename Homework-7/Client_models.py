from socket import AF_INET, SOCK_STREAM, socket, SOL_SOCKET, SO_REUSEADDR
import time
import pickle
import logging

import log.client_log_config

logger = logging.getLogger('client')


class ClientSocket:

    def client(self, msg, name, password, param, soc):
        logger.info(f'Начинается отправка сообщения на сервер.')
        # self.soc.connect(('localhost', self.port))
        try:
            if param == '2':
                data = soc.recv(1024).decode('utf-8')
                print(data)
                logger.info(f'Сообщение получено {data}')
            elif param == '1':
                try:
                    # self.soc.connect(('localhost', self.port))
                    soc.send(msg.encode('utf-8'))
                    logger.info(f'Сообщение отправлено {msg}')
                except pickle.PickleError:
                    logger.error('Не удалось сообщни серверу')
                    soc.close()
            elif param == '3':
                logger.error('Отключение успешно')
                soc.close()

        except ConnectionRefusedError:
            logger.critical('Ошибка соеденинения')
