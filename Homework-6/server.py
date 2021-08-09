from Server_models import *
import logging
import log.server_log_config
logger = logging.getLogger('server')
from deco import logdec

@logdec
def server() -> None:
    logger.info(f'Начало инициализации')
    start_server = ServerSocket()
    logger.info(f'Старт Сервер')
    start_server.server()


if __name__ == '__main__':
    try:
        logger.info(f'Запуск функции сервера')
        server()
    except Exception as ans:
        logger.critical(f'Ошибка запуска {ans}')
