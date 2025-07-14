def lowercase_decorator(function):
    def wrapper():
        func = function()
        string_lowercase = func.lower()
        return string_lowercase
    return wrapper

def splitter_decorator(function):
    def wrapper():
        func = function()
        string_spitter = func.split()
        return string_spitter
    return wrapper

@lowercase_decorator
@splitter_decorator

def hello():
    return "Hello World"

print(hello())