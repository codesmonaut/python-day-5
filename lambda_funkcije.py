# Operacije:

# # 1. Transformacija ili mapiranje:

# def transformacija (x):
#     return x ** 2 + 1

# ulaz = [1, 2, -1, 3]

# izlaz = []

# for x in ulaz:
#     y = transformacija(x)

#     izlaz.append(y)

# izlaz = list(map(transformacija, ulaz))

# izlaz = list(map(lambda x : x ** 2 + 1, ulaz))

# print(izlaz)

# # 2. Filtriranje:

# ulaz = [1, 4, 5, 10, 9, -6 , 13]
# print(ulaz)

# izlaz = list(filter(lambda x: x % 2 == 1, ulaz))
# print(izlaz)

# 3. Redukcija ili agregacija:

ulaz = [1, 3, -2, 6]

suma = 0

for x in ulaz:
    suma += x

print(suma)

# Koriscenjem funkcije redukcije:

import functools

suma = functools.reduce(lambda x, medjusuma : medjusuma + x, ulaz, 0)
print(suma)