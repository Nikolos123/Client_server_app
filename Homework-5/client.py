from Client_models import *
import logging

logger = logging.getLogger('mes.client')

def main() ->None:
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
        main()
    except Exception as ans:
        logger.critical('Ошибка запуска')
