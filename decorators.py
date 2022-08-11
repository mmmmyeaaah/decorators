from datetime import datetime

def decorate(func, path=input('Введите имя папки, в которую сохранить логи: ')):

    def _decorate():
        def log():
            res = func()
            time = datetime.now()
            name = func.__name__
            arguments = func.__code__.co_varnames
            my_list = [time, name, arguments, res]
            with open(path + '/log_file.log', 'a') as log_file:
                for arg in my_list:
                    log_file.write(str(arg) + '\n')

        return log()  
    return _decorate()