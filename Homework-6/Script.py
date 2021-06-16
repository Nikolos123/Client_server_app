# Типы декораторов:
# def dec1(func):
# """Декоратор не принимает и не передает аргументов"""
# return func
# def dec2(func):
# """Декоратор может принимать аргументы для декорируемой функции"""
# @wraps(func)
# def wrapper(*args, **kwargs):
# return func(*args, **kwargs)
# return wrapper
#
# def dec3(timeout):
# """Декоратор может принимать аргументы для себя и для декорируемой функции"""
# def func_caller(func):
# @wraps(func)
# def wrapper(*args, **kwargs):
# return func(*args, **kwargs)
# return wrapper
# return func_caller  1 час



@log
def func_z():
 pass

def main():
 func_z()