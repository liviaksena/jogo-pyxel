import pyxel

class Jogador:

    def __init__(self):
        self.x = 80
        self.y = 60
        self.largura = 10
        self.altura = 10
        self.velocidade = 2

    def atualizar(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= self.velocidade

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += self.velocidade

        if pyxel.btn(pyxel.KEY_UP):
            self.y -= self.velocidade

        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += self.velocidade

        self.x = max(0, min(self.x, 160 - self.largura))
        self.y = max(0, min(self.y, 120 - self.altura))

    def desenhar(self):
        pyxel.rect(self.x, self.y, self.largura, self.altura, 11)