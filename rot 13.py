
def rot13(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return "".join([alphabet[(alphabet.find(x) + 13) % 26] for x in message])


print(rot13("Grfg"))




