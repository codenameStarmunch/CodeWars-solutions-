def even_or_odd(s):
    evens = []
    odds = []

    for x in list(map(int, s)):
        if x % 2 == 0:
            evens.append(x)
        if x % 2 ==1:
            odds.append(x)

    if sum(evens) > sum(odds):
        return "Even is greater than Odd"
    if sum(evens) < sum(odds):
        return "Odd is greater than Even"
    return "Even and Odd are the same"


print(even_or_odd('1232'))