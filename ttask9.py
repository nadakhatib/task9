class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def display(self):
        print("Length:", self.length)
        print("Width:", self.width)
        print("Perimeter:", self.perimeter())
        print("Area:", self.area())


class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def display(self):
        super().display()
        print("Height:", self.height)
        print("Volume:", self.volume())



rectangle = Rectangle(6, 4)
rectangle.display()

print("****************** ")

parallelepiped = Parallelepipede(4, 2, 6)
parallelepiped.display()
