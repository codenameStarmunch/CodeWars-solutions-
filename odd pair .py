# Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other (that is, they are distinct).

def odd_pair(input):
    for x in input:
        for y in input:
            if (x != y) and (x * y % 2 ==1):
                return x, y
    return "Spam"


print(odd_pair([1, 3, 3, 45, 56, 54, 7, 8, 98, 70]))