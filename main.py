from decorators import decorate


if __name__ == '__main__':
    @decorate
    def get_name(name='Vic'):
        return f'Hello, {name}!'