class Figure:
    sides_count = 0

    def __init__(self, color, sides):
        self.__sides = sides
        self.__color = color



    def get_color(self):
        return self.__color

    def __is_valid_color(self, r,g,b):
        if  0 <=r  <= 255 and  0  <= g <= 255 and 0 <= b <= 255:
            print("Цвет подобран верно, можно менять")
            return True

    def set_color(self, r, g, b):
       if self.__is_valid_color(r, g, b):
           self.__color = [r, g, b]
       else:
           print("Цвет нельзя изменить, данные некорректры. Измените значеня.")

    def __is_valid_side(self, sides):
        # Проверка каждой стороны: положительное целое число
        for side in sides:
            if not isinstance(side, int) or side < 0:
                return False
        return True

    def get_sides(self):
        return self.__sides
    def __len__(self):
        # Возвращаем периметр фигуры
        return sum(self.__sides)

    def set_sides(self, new_sides):
        if len(new_sides) != self.sides_count:
            print(
                f"Количество сторон не совпадает с ожидаемым ({self.sides_count}). Устанавливаем стандартные стороны.")
            self.__sides = [1] * self.sides_count
        elif self.__is_valid_side(new_sides):
            self.__sides = new_sides
            print(f"Стороны изменены на {new_sides}")
        elif self.sides_count == 12:
            self.__sides = [1] * self.sides_count

        else:
            print("Некорректные значения сторон.")
class Circle(Figure):
    sides_count = 1  # У круга всегда одна сторона (1 условная единица)

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__radius = sides * 2


    def get_square(self):
        return self.__radius

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, sides):
        super().__init__(color, sides)

    def get_square(self):
        sides =self.get_sides() # Вызываем функцию в которюпередаются стороны из нашего класса и приравниваем ее
        # к переменной
        if len(sides) == 3: #если наши стороны равны трем тогда присваем их к аждому значению для удобства расчета
            # по формуле
            a,b,c = sides
            print(f"Стороны треугольника: a = {a}, b = {b}, c = {c}") #проверяем все ли значения верны чтоб убедиться
            # чтоб подставить расчеты для вычесления площади треугольника
            p = 0.5 * sum(sides)
            P = p * (p - a)*(p - b)*(p - c)
            S = P ** 0.5
            return f"Площадь треугольника равна: {S}"


class Cube(Figure):
    sides_count = 12
    def __init__(self, color, sides):
        super().__init__(color, sides)



    def get_volume(self):
        return self.sides_count



print("###########################")
print('Проверяем Круг')
print("###########################")

circle1 = Circle((200, 200, 100), 12) # (Цвет, стороны)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
print(circle1.get_sides())
circle1.set_sides([15]) # Изменится
print(circle1.get_sides())# Проверка на изменение сторон:
circle1.set_sides([5,2,4])  # Передача списка значений
print(circle1.get_sides())
print(circle1.get_square())
print(len(circle1))
print("###########################")
print('Дальше все про Треугольник')
print("###########################")
triangle = Triangle((200, 200, 100), [12, 12, 14]) # (Цвет, стороны)
triangle.set_color(55, 669, 77) # Изменится
print(triangle.get_color())
print(triangle.get_sides())
triangle.set_sides([15]) # Изменится
print(triangle.get_sides())# Проверка на изменение сторон:
triangle.set_sides([5,2,4])  # Передача списка значений
print(triangle.get_sides())
print(triangle.get_square())
print("###########################")
print('Дальше все про Куб')
print("###########################")
cube1 = Cube((222, 35, 130), 6)
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
print(cube1.get_volume())

