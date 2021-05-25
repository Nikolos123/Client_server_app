# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

def main():
    # Можно было сделать просто через принт a= b'класс'
    # и так как мы не указываем явно кодировку используется по умолчанию ASCII что ниже я исделал
    # через try я получаю ошибку и except выдаю print

    worlds = ['attribute', 'класс', 'функция', 'type']
    for i in worlds:
        try:
            asn = bytes(i, encoding='ASCII')
            print(f'это слово возможно записать в байтовом типе {asn}')
        except Exception as ans:
            print(f'это слово невозможно записать в байтовом типе "{i}"')


if __name__ == '__main__':
    try:
        main()
    except Exception as ans:
        print(ans)
