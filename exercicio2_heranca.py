import math

class FiguraGeometrica:
    def __init__(self):
        pass


class Retangulo(FiguraGeometrica):
    def __init__(self,base= "", altura=""):
        super().__init__()
        self._base       = base
        self._altura    = altura

    def calcular_area(self):
        return self._base * self._altura


class Circulo(FiguraGeometrica):
    def __init__(self,raio=""):
        super().__init__()
        self._raio      = raio

    def calcular_area(self):
        return math.pi * (self._raio ** 2)



class Triangulo(FiguraGeometrica):
    def __init__(self,base="", altura=""):
        super().__init__()
        self._base      = base
        self._altura    = altura 

    def calcular_area(self):
        return self._base * self._altura/2

ret1     = Retangulo(base=5,altura=10)
cir1    = Circulo(raio=5)
tri1     = Triangulo(base=10,altura=5)

print()
print("Área do Retângulo:", ret1.calcular_area())
print("Área do Círculo:", cir1.calcular_area())
print("Área do Triângulo:", tri1.calcular_area())