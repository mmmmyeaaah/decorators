from decorators import decorate

@decorate()
def flat_generator(list_):
    for words in list_:
        for word in words:
            yield word


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

if __name__ == '__main__':
    for item in flat_generator(nested_list):
	    print(item) 