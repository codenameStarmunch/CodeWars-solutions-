
def tetrad(n):
    if type(n) is not int:
        return None

    return [int(n), float(n), str(n), tuple([n])]


print(tetrad(33))