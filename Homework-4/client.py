from Client_models import *


def main():
    while True:
        # Ну тут уже можно задавать любые функции и обрабатывать их
        name = input(' Введите name ')
        password = input(' Введите password ')
        # message = input(' Введите сообщение ')
        start_client = ClientSocket()
        start_client.client('', name, password)


if __name__ == '__main__':
    try:
        main()
    except Exception as ans:
        print(ans)
