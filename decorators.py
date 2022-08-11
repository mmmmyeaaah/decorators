from datetime import datetime

def decorate(path=input('Введите имя папки, в которую сохранить логи: ')):

    def _decorate(func):

        def log(*args, **kwargs):
            with open(path + '/log_file.log', 'a', encoding='UTF-8') as log_file:
                res = func(*args, **kwargs)
                log_file.write(f'Имя функции: {func.__name__}' + '\n')
                log_file.write(f'Время вызова: {datetime.now()}' + '\n')
                log_file.write(f'Аргументы функции: {args}' + '\n')
                log_file.write(f'Вернула значение: {res}' + '\n')
            return res

        return log

    return _decorate