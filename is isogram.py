
def is_isogram(string):
    for x in string:
        if string.count(x) > 1:
            return False
    return True
  

print(is_isogram("aba"))