def dodawanie(a, b):
    return a + b


def odejmowanie(a, b):
    return a - b


def mnożenie(a, b):
    return a * b


def dzielenie(a, b):
    return a / b


print("Wybierz działanie")

print("1 - dodawanie")

print("2 - odejmowanie")

print("3 - mnozenie")

print("4 - dzielenie")

while True:

    n = int(input())

    if n == 0:
        print("Dziekujemy za korzystanie z kalkulatora. Zapraszamy ponownie")

        break

    if n == 1:
        print("Podaj 2 liczby")

        k = int(input())

        l = int(input())

        print(dodawanie(k, l))

    if n == 2:
        print("Podaj 2 liczby")

        k = int(input())

        l = int(input())

        print(odejmowanie(k, l))

    if n == 3:
        print("Podaj 2 liczby")

        k = int(input())

        l = int(input())

        print(mnozenie(k, l))

    if n == 4:

        print("Podaj 2 liczby")

        k = int(input())

        l = int(input())

        print(dzielenie(k, l))

    else:

        print("Prosze podać liczbę z zakresu 0 - 4")