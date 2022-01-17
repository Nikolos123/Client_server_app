from functools import wraps
import logging

from inspect import currentframe, getouterframes, stack
import traceback


def logdec(func):
    if func.__name__ == 'client':
        import log.client_log_config
        logger = logging.getLogger('client')
    else:
        import log.server_log_config
        logger = logging.getLogger('server')

    @wraps(func)
    def wrapper(*args, **kwargs):
        # modul_name = traceback.StackSummary.extract(traceback.walk_stack(None))[0].name
        modul_name = getouterframes(currentframe())[1][3]

        logger.info(
            f'Функция с именем {func.__name__} вызвана, аргумент {args},'
            f'{kwargs}. Вызов из {modul_name}.')
        return func(*args, **kwargs)

    return wrapper
