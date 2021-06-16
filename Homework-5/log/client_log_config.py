import logging

# added format messages
_format = logging.Formatter(
    '%(asctime)-10s %(levelname)-10s %(module)s %(message)s')
# added file_name count_copy and other params

log_handler = logging.FileHandler('log/client.log', encoding='utf-8')
log_handler.setFormatter(_format)
# need import  in modul for work
logger = logging.getLogger('client')
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

if __name__ == '__main__':
    start = logging.StreamHandler()
    start.setLevel(logging.DEBUG)
    start.setFormatter(_format)
    logger.addHandler(start)
    logger.info('client')
