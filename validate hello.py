
def validate_hello(greetings):
    words = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']

    for x in words:
        if x in greetings.lower():
            return True
    return False


print(validate_hello("meh"))