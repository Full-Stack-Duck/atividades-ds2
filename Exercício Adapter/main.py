class Quadrado:
    def __init__(self, lado: int) -> None:
        self.lado = lado

    def calcular_area(self) -> int:
        return self.lado ** 2

class QuadradoParaRaio:
    def __init__(self, quadrado: Quadrado) -> None:
        self.quadrado = quadrado

    def calcular_area(self) -> float:
        return self.quadrado.calcular_area() * 2 * 3.14

def calcular_area(forma):
    return forma.calcular_area()

quadrado = Quadrado(10)
print(f"Resultado do cálculo do Quadrado: {calcular_area(quadrado)}")

circulo = QuadradoParaRaio(quadrado)
print(f"Resultado do cálculo do Circulo: {calcular_area(circulo)}")