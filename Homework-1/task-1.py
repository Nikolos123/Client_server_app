# Каждое из слов «разработка», «сокет», «декоратор» представить в строковом
# формате и проверить тип и содержание соответствующих переменных.
# Затем с помощью онлайн-конвертера преобразовать строковые представление в формат
# Unicode и также проверить тип и содержимое переменных.и

def main():
    worlds = ['разработка', 'сокет', 'декоратор']

    for s in worlds:
        print(f'имя : {s}')
        print(f'тип : {type(s)}')

    converter = ['\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0',
                 '\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82',
                 '\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80']

    for b in converter:
        print(f'имя : {b.encode()}')
        print(f'тип : {type(b)}')


if __name__ == '__main__':
    try:
        main()
    except Exception as ans:
        print(ans)
