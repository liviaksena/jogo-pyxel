import pyxel

class Tiro:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.largura = 2
        self.altura = 5
        self.velocidade = 4

    def atualizar(self):
        self.y -= self.velocidade

    def desenhar(self):
        pyxel.rect(self.x, self.y, self.largura, self.altura, 10)