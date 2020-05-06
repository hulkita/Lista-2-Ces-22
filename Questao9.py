class Shape:
    geometric_type = 'Generic_Shape'

    def area(self):
        raise NotImplementedError

    def get_geometric_type(self):
        return self.geometric_type

class Plotter:
    def plot(self, ratio, topleft):
        print('Plotting at {} , ratio{}.'.format(topleft, ratio))

class Polygon(Shape, Plotter):
    geometric_type = 'Polygon'


class RegularPolygon(Polygon):
    geometric_type = 'Regular Polygon'

    def __init__(self, side):
        self.side = side
class RegularHexagon(RegularPolygon):
    geometric_type = 'RegularHexagon'

    def area(self):
        return 1.5 * (3 ** .5 * self.side ** 2)

class Square(RegularPolygon):
    geometric_type = 'Square'

    def area(self):
        return self.side * self.side

class Triangulo(RegularPolygon):
    geometric_type = 'Triangulo'

    def area(self):
        return self.side * self.side * pow(3, 0.5) / 4

class draw_square_onto_a_triangle(Square, Triangulo):

    def draw(self):
        print("Here we have a triangle within a square")



"""Primeiro Caso : classe derivada de duas outras classes"""
poligonogenerico = Polygon()
print(poligonogenerico.__class__.mro())

"""Segundo Caso: classe derivada de uma classe que é derivado de outras duas classes"""
poligono_regular = RegularPolygon(10)
print(poligono_regular.__class__.mro())

"""Tericeiro Caso: A classe 'draw_square_onto_a_triangle' que deriva de outras
 duas classes 'Triangulo' e 'Square' que derivam ambas da classeRegularHexagon"""

A = Square(10)
B = Triangulo(10)
C = draw_square_onto_a_triangle(10)
print(C.__class__.mro())





