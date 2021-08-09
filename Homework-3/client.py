from ClientServer import *


def main():
    # Ну тут уже можно задавать любые функции и обрабатывать их
    name = input(' Введите name ')
    password = input(' Введите password ')
    # message = input(' Введите сообщение ')
    start_client = ClientServerSocket()
    start_client.client('', name, password)


if __name__ == '__main__':
    try:
        main()
    except Exception as ans:
        print(ans)
