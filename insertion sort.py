
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key


lst = [3, 5, 6, 12, 34, 4, 2]
insertion_sort(lst)
print(f"Sorted list: {lst}")
