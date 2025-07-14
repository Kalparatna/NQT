def names_decoder(function):
    def wrapper(a, b):
        a = a.capitalize()
        b = b.capitalize()

        string_hello = function(a, b)
        return string_hello
    return wrapper

@names_decoder

def hello(a, b):
    return "hello " + a + ", Hello " + b

print(hello("Ajay", "Sunny"))