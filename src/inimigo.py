import pyxel

class Inimigo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.largura = 10
        self.altura = 10
        self.velocidade = 1

    def atualizar(self):
        self.y += self.velocidade

    def desenhar(self):
        pyxel.rect(self.x, self.y, self.largura, self.altura, 8)