from Client_models import *
import logging
import log.client_log_config
logger = logging.getLogger('client')
from deco import logdec

@logdec
def client() ->None:
    while True:
        # Ну тут уже можно задавать любые функции и обрабатывать их
        name = input(' Введите name ')
        password = input(' Введите password ')
        # message = input(' Введите сообщение ')
        logger.info(f'Начало инициализации')
        start_client = ClientSocket()
        logger.info(f'Отправка данных на сервер')
        start_client.client('', name, password)


if __name__ == '__main__':
    try:
        logger.info(f'Запуск Клиента')
        client()
    except Exception as ans:
        logger.critical(f'Ошибка запуска {ans}')
