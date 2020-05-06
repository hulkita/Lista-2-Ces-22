class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def reflect_x(self):
        self.y = - self.y

