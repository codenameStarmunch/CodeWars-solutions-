
def flatten_and_sort(array):
    return [x for y in array for x in y]


print(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]))