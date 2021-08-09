# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в
# байтовое и выполнить обратное преобразование (используя методы encode и decode).

def main():
    worlds = ['разработка', 'администрирование', 'protocol', 'standard']

    for i in worlds:
        a = i.encode(encoding='utf-8')
        print(a)
        print(a.decode(encoding='utf-8'))


if __name__ == '__main__':
    try:
        main()
    except Exception as ans:
        print(ans)
