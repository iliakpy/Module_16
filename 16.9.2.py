"""
Напишите код для описания геометрической фигуры.
Создайте класс «прямоугольник» с помощью метода  __init__().
На выходе в консоли вам необходимо получить длину и ширину с итоговыми значениями.
"""

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b


Fig = Rectangle(5, 15)
print(Fig.get_area())