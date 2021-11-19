
# Method 1: 


import re

def triple_x(s):
    return bool(re.match(r"[^x]*xxx", s))


print(triple_x("abraxxxas"))


# Method 2: 


def triple_x(s):
    for x in range(len(s)):
        if s[x] == 'x':
            return s[x+1:x+3] == 'xx'

    return 0


print(triple_x("abraxxxas"))


# Method 3:


def triple_x(s):
    return s.find("xxx") == s.find("x") != -1


print(triple_x("abraxxxas"))