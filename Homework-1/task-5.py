# Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
# байтовового в строковый тип на кириллице.

import subprocess


def main():
    all_list = []
    all_list.append(['ping', 'yandex.com'])
    all_list.append(['ping', 'youtube.com'])

    for i in all_list:
        subproc_ping = subprocess.Popen(i, stdout=subprocess.PIPE)
        for line in subproc_ping.stdout:
            print(line.decode(encoding='cp866'))


if __name__ == '__main__':
    try:
        main()
    except Exception as ans:
        print(ans)
