from threading import Thread

from Client_models import *
import logging
import log.client_log_config
from socket import AF_INET, SOCK_STREAM, socket

logger = logging.getLogger('client')
from deco import logdec


@logdec
def client() -> None:
    with socket(AF_INET, SOCK_STREAM) as soc:
        logger.info(f'Инициализация сокета прошла успешна.')
        soc.connect(('localhost', 7777))
        start_client = ClientSocket()
        while True:

            print(
                f'Если вы хотите отправить сообщения нажми 1 \nЕсли вы хотите получить сообщения нажми 2 \nЕсли вы хотите прекратить общение нажмите 3')
            ans = input('Введите выбранный вариант ')
            if ans == '1':
                # Ну тут уже можно задавать любые функции и обрабатывать их
                message = input(' Введите сообщение ')
                logger.info(f'Начало инициализации отправки сообщения')
                logger.info(f'Отправка данных на сервер для отправки сообщения')
                start_client.client(message, '', '', ans, soc)
            elif ans == '2':
                logger.info(f'Начало инициализации отправки сообщения')
                logger.info(f'Получить ответ на сообщения')
                start_client.client('', '', '', ans, soc)
            elif ans == '3':
                logger.error('Отключение успешно')
                break
            else:
                logger.error(f'Выбранный вариант ответа не существует в системе ')


if __name__ == '__main__':
    try:
        logger.info(f'Запуск Клиента')
        read_write = Thread(target=client())
    except Exception as ans:
        logger.critical(f'Ошибка запуска {ans}')
