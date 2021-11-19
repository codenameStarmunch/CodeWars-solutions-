
def reversed_words(string):
    return " ".join(string.split()[::-1])


print(reversed_words("The greatest victory is that which requires no battle"))