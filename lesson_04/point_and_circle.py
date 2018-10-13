class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '({}, {}, {})'.format(self.x, self.y, self.z)


point = Point(3, 4, 5)
print(point)


class Circle(Point):

    def __init__(self, x, y, z, radius):
        super().__init__(x, y, z)
        self.radius = radius

    def __str__(self):
        return '({}, {}, {}) with radius: {}'.format(self.x, self.y, self.z, self.radius)


circle = Circle(3, 4, 4, 8)
print(circle)

