
def order(words):
  return " ".join(sorted(words.split(), key=lambda x: sorted(x)))

print(order("is2 Thi1s T4est 3a"))

