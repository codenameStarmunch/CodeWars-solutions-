
def bubble_sort(lst):
    for x in range(len(lst)):
        for y in range(0, len(lst) - x -1):
            if lst[y] > lst[y + 1]:
                lst[y], lst[y + 1] = lst[y + 1], lst[y]


lst = [3, 2, 1, 5, 4, 56]
bubble_sort(lst)

print(f"Sorted list: {lst}")