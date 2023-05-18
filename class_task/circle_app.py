import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area_of_circle(self):
        return f"Area of the circle is {math.pi * (self.radius ** 2)}"

    def circumference_of_circle(self):
        return f"cprint(n)print(n)print(n)ircumference of the circle is {2 * math.pi * self.radius}"


cal = Circle(5)
print(cal.area_of_circle())

print(cal)
