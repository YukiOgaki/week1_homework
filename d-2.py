import math


class Rectangle:
    # コードが期待通り動作するように実装
    def __init__(self, height: float, width: float):
        self.height = height
        self.width = width

    def area(self):
        area_rectangle = self.height * self.width
        return f"{area_rectangle:.2f}"

    def diagonal(self):
        diagonal_rectangle = math.sqrt(self.height**2 + self.width**2)
        return f"{diagonal_rectangle:.2f}"


rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area())  # 30.00
print(rectangle1.diagonal())  # 7.81

rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area())  # 9.00
print(rectangle2.diagonal())  # 4.24
