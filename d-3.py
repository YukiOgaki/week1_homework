import math


class Square:
    # コードが期待通り動作するように実装
    def __init__(self, side):
        self.side = side

    def area(self):
        area_rectangle = float(self.side) ** 2
        if area_rectangle == int(area_rectangle):
            return int(area_rectangle)
        else:
            return f"{area_rectangle:.2f}"

    def diagonal(self):
        diagonal_rectangle = float(self.side) * math.sqrt(2)
        return f"{diagonal_rectangle:.2f}"


square1 = Square(side=1.5)
print(square1.area())  # 2.25
print(square1.diagonal())  # 2.12

square2 = Square(side=15)
print(square2.area())  # 225
print(square2.diagonal())  # 21.21
