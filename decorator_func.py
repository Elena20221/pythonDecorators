from datetime import datetime
import hashlib


def get_log(func):
    def foo(*args, **kwargs):
        date_time = datetime.now()
        func_name = func.__name__
        result = func(*args, **kwargs)
        with open('decoratorlogs.txt', 'w', encoding='utf-8') as file:
            file.write(f'Дата/время: {date_time}\n'
                       f'Имя функции: {func_name}\n'
                       f'Аргументы: {args, kwargs}\n'
                       f'Результат: {result}\n')
        return result
    return foo


@get_log
def get_hash(path: str):
    with open(path) as file:
        for line in file:
            yield hashlib.md5(line.encode()).hexdigest()


if __name__ == '__main__':
    get_hash('wiki_links.txt')