class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_line_to(self, point):
        a = (self.y - point.y) / (self.x - point.x)

        b = self.y - (a * self.x)
        c = (a, b)
        return c


ponto1 = Point(2, 2)
ponto2 = Point(5, 5)

print(ponto1.get_line_to(ponto2))



