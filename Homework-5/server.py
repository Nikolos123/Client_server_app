from Server_models import *
import logging
import log.server_log_config
logger = logging.getLogger('server')

def main() -> None:
    logger.info(f'Начало инициализации')
    start_server = ServerSocket()
    logger.info(f'Старт Сервер')
    start_server.server()


if __name__ == '__main__':
    try:
        logger.info(f'Запуск функции сервера')
        main()
    except Exception as ans:
        logger.critical(f'Ошибка запуска {ans}')
