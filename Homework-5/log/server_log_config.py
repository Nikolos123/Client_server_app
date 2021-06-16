import logging
from logging.handlers import TimedRotatingFileHandler

# added format messages
_format = logging.Formatter(
    '%(asctime)-10s %(levelname)-10s %(module)s %(message)s')
# added file_name count_copy and other params

log_handler = TimedRotatingFileHandler('server.log', when='D',
                                       backupCount=20)
log_handler.setFormatter(_format)

logger = logging.getLogger('mes.server')
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

if __name__ == '__main__':
    start = logging.StreamHandler()
    start.setLevel(logging.DEBUG)
    start.setFormatter(_format)
    logger.addHandler(start)
    logger.info('server')
