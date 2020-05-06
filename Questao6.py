class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def slope_from_origin(self):
        slope = self.y / self.x
        return slope

    