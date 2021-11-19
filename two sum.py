

def two_sum(numbers, target):
    hash_list = {}

    for x in range(len(numbers)):
        pair = target - numbers[x]

        if pair in hash_list:
            return (x, hash_list[pair])
        else:
            hash_list[numbers[x]] = x

    return None


print(two_sum([2,2,3], 4))


