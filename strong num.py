
def strong_num(number):
    sum = 0
    integer = number

    while(integer > 0):
        factorial = 1
        x = 1
        remainder = integer % 10

        while(x <= remainder):
            factorial = factorial * x
            x = x + 1
        sum +=  factorial
        integer = integer // 10

    if (sum == number):
        return f"{number} is a Strong Number"
    else:
        return f"{number} is not a Strong Number"




print(strong_num(145))