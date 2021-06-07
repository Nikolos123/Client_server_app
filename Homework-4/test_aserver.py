from time import sleep

from ClientServer import *


def main():
    # test_error_server()
    test_server()


# def test_error_server():
#     start_server = ClientServerSocket()
#     start_server.server('test')


def test_server():
    start_server = ClientServerSocket()
    print(start_server.server('test'))


if __name__ == '__main__':
    try:
        main()
    except Exception as ans:
        print(ans)
