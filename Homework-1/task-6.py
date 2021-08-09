# Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
# Проверить кодировку файла по умолчанию.
# Принудительно открыть файл в формате Unicode и вывести его содержимое
import locale


def main():
    worlds = ['сетевое программирование', 'сокет', 'декоратор']
    with open('test_file.txt', 'w') as ans:
        for i in worlds:
            ans.write(f'{i}\n')

    file_coding = locale.getdefaultlocale()

    with open('test_file.txt', 'r', encoding=file_coding[1]) as f:
        print(f.read())


if __name__ == '__main__':
    try:
        main()
    except Exception as ans:
        print(ans)
