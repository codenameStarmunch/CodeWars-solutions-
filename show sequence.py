
def show_sequence(n):
    final = ""
    iter = sum((x + x) - x for x in range(0, n + 1))

    if n < 0:
        final += f"{n}<0"
    if n == 0:
        final += f"{n}=0"
    else:
        for x in range(0, n + 1):
            if x != n:
                final += f"{x}+"
            else:
                final += f"{x} = {iter}"

    return final


print(show_sequence(-1))

