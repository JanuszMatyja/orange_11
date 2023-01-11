def wykonaj(funkcja, a, b):
    x = funkcja(a, b)
    return x

def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a -b

print(wykonaj(dodaj, 2, 3))
print(wykonaj(odejmij, 4, 3))