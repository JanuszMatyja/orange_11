import math


class MyFirstClass:
    def __int__(self,
                x=0,
                y=0):
        '''
        Inicjalizacja zmiennych klasowych
        :param x: Liczba float
        :param y: Liczba float
        '''
    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
   def reset(self):
       self.move(0, 0)

  def calculate(self, other: "MyFirstClass") -> float:
      return math.hypot(self.x - other.x, self.y - other)

a = MyFirstClass()
b = MyFirstClass()
a.x = 5
a.y = 4
b.x = 3
b.y = 6
a.reset()
b.move(5, 0)
print(b.calculate(a))

# print(a)
# print(b)
