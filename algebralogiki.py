print(f'Пример 1')
for a in 0, 1:
  for b in 0, 1:
    for c in 0, 1:
        F = not (a or b) and c
        print(a, b, c, F)

print(f'Пример 2')
for x in 0, 1:
  for y in 0, 1:
    for z in 0, 1:
        F = (not x and not y) <= z
        print(x, y, z, F)

print(f'Пример 3')
for S1 in 0, 1:
  for S2 in 0, 1:
    for S3 in 0, 1:
        F = (S1 and not S2) or S3
        print(S1, S2, S3, F)

print(f'Пример 4')
for x in 0, 1:
  for y in 0, 1:
    for z in 0, 1:
        F = (not x) == (y or z)
        print(x, y, z, F)

print(f'Пример 5')
for a in 0, 1:
  for b in 0, 1:
    for c in 0, 1:
        F = a <= (b or not c)
        print(a, b, c, F)

print(f'Пример 6')
for a in 0, 1:
  for b in 0, 1:
    for c in 0, 1:
        F = (not (a and b)) or c
        if F == 0:
            print(a, b, c, F)

print(f'Пример 7')
for x1 in 0, 1:
  for x2 in 0, 1:
    for x3 in 0, 1:
        F = (not x1 and not x2) or (x1 and x2)
        print(x1, x2, x3, F)

print(f'Пример 8')
for a in 0, 1:
  for b in 0, 1:
    for c in 0, 1:
        F = (a and not c) == (not (a and b))
        print(a, b, c, F)
