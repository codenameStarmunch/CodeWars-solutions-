
def create_phone_number(n):
    numbers = "".join(map(str, n))

    return "(" + numbers[0:3] +") " +  numbers[3:6] + "-" + numbers[6::]



print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))  # (123) 456-7890