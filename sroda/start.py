from pakiet import kalkulator

designs = ['telefon', 'robot', 'sześcian']
models = []

global_adj: float
global_adj = 3.6


def some_fun(a: float, b: float, t: float) -> float:
    return a + b * t + global_adj


(print(some_fun(4, 3, 2)))