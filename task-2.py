# Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность
# кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

def main():
    worlds = ['class', 'function', 'method']

    for i in worlds:
        print(f'имя : {bytes(i, encoding="utf-8")}')
        print(f'тип : {type(bytes(i, encoding="utf-8"))}')


if __name__ == '__main__':
    try:
        main()
    except Exception as ans:
        print(ans)
