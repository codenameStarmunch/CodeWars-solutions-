
import itertools

neighbours = ("08", "124", "1235", "236", "1457", "24568", "3569", "478", "05789", "689")

def get_pins(observed):
    return ["".join(x) for x in itertools.product(*(neighbours[int(y)]for y in observed))]


print(get_pins("7"))

