import pyxel

from src.tiro import Tiro

class Jogador:

    def __init__(self):
        self.x = 80
        self.y = 60
        self.largura = 10
        self.altura = 10
        self.velocidade = 2
        self.tiros = []

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

        if pyxel.btnp(pyxel.KEY_SPACE):
            self.atirar()

        for tiro in self.tiros[:]:
            tiro.atualizar()
            if tiro.y < 0:
                self.tiros.remove(tiro)
                
    def atirar(self):
        x = self.x + self.largura // 2 - 1
        y = self.y

        tiro = Tiro(x, y)
        self.tiros.append(tiro)


    def desenhar(self):
        pyxel.rect(self.x, self.y, self.largura, self.altura, 11)
        
        for tiro in self.tiros:
            tiro.desenhar()