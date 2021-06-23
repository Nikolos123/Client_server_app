from Client_models import *
import logging
import log.client_log_config
logger = logging.getLogger('client')
from deco import logdec

@logdec
def client() ->None:
    name = input(' Введите name ')
    password = input(' Введите password ')
    while True:
        print(f'Если вы хотите отправить сообщения нажми 1 \n Если вы хотите получить сообщения нажми 2')
        ans = input('Введите выбранный вариант ')
        if ans =='1':
            # Ну тут уже можно задавать любые функции и обрабатывать их
            message = input(' Введите сообщение ')
            logger.info(f'Начало инициализации отправки сообщения')
            start_client = ClientSocket()
            logger.info(f'Отправка данных на сервер для отправки сообщения')
            start_client.client(message, name, password,ans)
        elif ans == '2':
            logger.info(f'Начало инициализации отправки сообщения')
            start_client = ClientSocket()
            logger.info(f'Отправка данных на сервер для отправки сообщения')
            start_client.client('',name,password,ans)

        else:
            logger.error(f'Выбранный вариант ответа не существует в системе ')


if __name__ == '__main__':
    try:
        logger.info(f'Запуск Клиента')
        client()
    except Exception as ans:
        logger.critical(f'Ошибка запуска {ans}')
