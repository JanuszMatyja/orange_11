generator_1 = (x for x in [1, 2, 3, 4, 5])

print(type(generator_1))
print(generator_1)

def generator_2():

    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

print(type(generator_2()))
print(next(generator_2()))
print("bla bla bla")
print(next(generator_2()))

