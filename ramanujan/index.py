def calculate_ramanujan():
  tried = {}
  a = 0
  b = 0

  while True:
    a += 1
    b = a
    while b > 0:
      result = a**3 + b**3
      if result in tried:
        c, d = tried[result]
        return f'{a}^3+{b}^3 = {c}^3+{d}^3 = {result}'
      else:
        tried[result] = (a, b)
      b -= 1

print(calculate_ramanujan())