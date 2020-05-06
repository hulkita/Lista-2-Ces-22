class Poligonos:
    def __init__(self, name):
        self.name = name

class Circulo(Poligonos):
    def draw(self):
        print("This function draws a circle.")

class Quadrado(Poligonos):
    def draw(self):
        print("This function draws a square.")

p1 = Quadrado(name = 'quadrado')
p2 = Circulo(name = 'circulo')

p1.draw()
p2.draw()

"""Neste exemplo de polimorfismo, o mesmo método draw executa
implementaçoes distintas para objetos de classes distintas um 
da classe Circulo e outro da classe Quadrado"""

def Desenhar(p):
    return p.draw()

Desenhar(p1)
Desenhar(p2)

"""A funçao acima (Desenhar) possui um exemplo de Duck Typing
uma vez que ao receber o objeto (p) executa o método 'draw'
sem se importar com o tipo do objeto"""