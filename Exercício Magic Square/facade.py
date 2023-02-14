from generator import Generator
from splitter import Splitter
from verifier import Verifier


class MagicSquareGenerator:
    def generate(self, size: int):
        generator = Generator()
        splitter = Splitter()
        verifier = Verifier()

        square = []
        while True:
            for i in range(size):
                linha = generator.generate(size)
                square.append(linha)
            s = splitter.split(square)
            teste = verifier.verify(s)
            if teste == True:
                return square
            else:
                square = []
