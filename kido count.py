
def kido_count(n):
  return [x for x in range(0, n + 1)  if x % 2 == 1]


print(kido_count(9))