import math


class Figure:
    CIRCLE_SIDES_COUNT = 1
    TRIANGLE_SIDES_COUNT = 3
    CUBE_SIDES_COUNT = 12

    def __init__(self, sides_count, color: tuple, *sides):
        if not self.__is_valid_color(*color):  # если неверно задан цвет то выход из программы
            print("Неверно задан цвет")
            exit()
        self.__color = list(color)
        self.sides_count = sides_count

        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:  # неправильное задание сторон - все будут единичные
            self.__sides = [1 for i in range(self.sides_count)]
        self.filled = False

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        if (0 <= r <= 255 and
                0 <= g <= 255 and
                0 <= b <= 255):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color[0] = r
            self.__color[1] = g
            self.__color[2] = b

    def __is_valid_sides(self, *sides):
        for x in sides:  # проверка на целочисленность и положительность длин сторон
            if not isinstance(x, int) or x <= 0:
                return False

        if len(sides) != self.sides_count:  # сторон передано больше или недостаточно
            return False

        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


# ---------------------------------------------------------------------------------------------
class Circle(Figure):
    def __init__(self, color: tuple, *sides):
        super().__init__(self.CIRCLE_SIDES_COUNT, color, *sides)
        self.__radius = self.get_sides()[0] / math.pi / 2

    def get_square(self):
        return math.pi * self.__radius ** 2


# ---------------------------------------------------------------------------------------------
class Triangle(Figure):
    def __init__(self, color: tuple, *sides):
        super().__init__(self.TRIANGLE_SIDES_COUNT, color, *sides)

    """Длина любой стороны треугольника меньше суммы длин двух других его сторон"""

    # def check_triangle_sides(self, *sides):
    #   p = len(self)
    #    for s in self.__sides[]

    def get_square(self):
        p = len(self) / 2
        m = p
        for s in self.get_sides():
            m *= p - s

        return math.sqrt(m)


# ---------------------------------------------------------------------------------------------
class Cube(Figure):
    def __init__(self, color: tuple, *sides):
        super().__init__(self.CUBE_SIDES_COUNT, color, *sides)
        # переопределим стороны
        if self.__is_valid_sides(*sides):
            self.set_sides(sides[0])
        else:  # неправильное задание сторон - все будут единичные
            self.set_sides(1)

    def get_volume(self):
        return self.get_sides()[0] ** 3

    def __is_valid_sides(self, *sides):
        for x in sides:  # проверка на целочисленность и положительность длин сторон
            if not isinstance(x, int) or x <= 0:
                return False

        if len(sides) != 1:  # для куба только 1 сторона
            return False

        return True

    # перепишем set_sides для куба, чтобы передавался только 1 параметр
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            Figure.set_sides(self, *[new_sides[0] for i in range(self.sides_count)])


# ---------------------------------------------------------------------------------------------

def main():
    circle1 = Circle((200, 200, 100), 2)  # (Цвет, стороны)
    circle2 = Circle((200, 200, 100), 10, 10)  # (Цвет, стороны)

    # цвета
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    circle1.set_color(300, 70, 15)  # Не изменится
    print(circle1.get_color())
    circle1.set_color(-1, 70, 15)  # Не изменится
    print(circle1.get_color())

    #Circle
    print("\nCircles")
    circle1.set_sides(-1)  # Не изменится
    print(circle1.get_sides())
    circle1.set_sides(10, 4)  # Не изменится
    print(circle1.get_sides())
    circle1.set_sides(10)  # изменится
    print(circle1.get_sides())
    print(circle1.get_square())
    print(len(circle1))
    print(circle2.get_sides()) #[1]

    #Triangles
    print("\nTriangles")
    t1 = Triangle((200, 200, 100), 5, 4, 3)
    t1.set_sides(5, 4, -3) # Не изменится
    print(t1.get_sides())
    t1.set_sides(5, 4, 0)  # Не изменится
    print(t1.get_sides())
    print(t1.get_square()) # 6
    t1.set_sides(1, 1, 2) # изменится
    print(t1.get_sides())

    t2 = Triangle((200, 200, 100), 1, 2, 3, 4)
    print(t2.get_sides())


    print("\nCubes")
    cube1 = Cube((222, 35, 130), 6)
    print(cube1.get_sides())

    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    cube1.set_sides(-1)  # Не изменится
    print(cube1.get_sides())
    cube1.set_sides(3)  # изменится
    print(cube1.get_sides())
    print(cube1.get_volume()) # 27


if __name__ == "__main__":
    main()
