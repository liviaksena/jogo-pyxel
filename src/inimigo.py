import pyxel

from src.sprite import SPRITES

class Inimigo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = SPRITES["inimigo1"]
        self.largura = self.sprite.largura
        self.altura = self.sprite.altura
        self.velocidade = 1

    def atualizar(self):
        self.y += self.velocidade

    def desenhar(self):
        pyxel.blt(self.x, self.y, self.sprite.imagem, self.sprite.u, self.sprite.v, self.sprite.largura, self.sprite.altura, colkey=0)

class GerenciaInimigos:
    def __init__(self):
        self.inimigos = []

    def adicionar_inimigo(self, inimigo):
        self.inimigos.append(inimigo)

    def atualizar_inimigos(self):
        for inimigo in self.inimigos:
            inimigo.atualizar()
            if inimigo.y > pyxel.height:
                self.inimigos.remove(inimigo)