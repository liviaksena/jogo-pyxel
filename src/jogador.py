import pyxel

from src.animation import Animate
from src.sprite import DURACAO_DEFAULT, SPRITES
from src.tiro import Tiro


class Jogador:

    def __init__(self):
        self.x = 80
        self.y = 100
        self.sprite = SPRITES["jogador"]
        self.largura = self.sprite.largura
        self.altura = self.sprite.altura
        self.velocidade = 3
        self.tiros = []
        self.turbina = TurbinaJogador()

    def atualizar(self):
        self.turbina.atualiza_animacao()

        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= self.velocidade

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += self.velocidade

        if pyxel.btn(pyxel.KEY_UP):
            self.y -= self.velocidade

        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += self.velocidade

        self.x = max(0, min(self.x, pyxel.width - self.sprite.largura))
        self.y = max(0, min(self.y, pyxel.height - SPRITES["player-card"].altura - self.sprite.altura))

        if pyxel.btnp(pyxel.KEY_SPACE):
            self.atirar()

        for tiro in self.tiros:
            tiro.atualizar()
            if tiro.y < 0:
                self.tiros.remove(tiro)
                
    def atirar(self):
        x = self.x + self.largura // 2 - 1
        y = self.y

        tiro = Tiro(x, y)
        self.tiros.append(tiro)


    def desenhar(self):
        self.turbina.desenha(self.x, self.y)
        pyxel.blt(self.x, self.y, self.sprite.imagem, self.sprite.u, self.sprite.v, self.sprite.largura, self.sprite.altura, colkey=0)

        
        for tiro in self.tiros:
            tiro.desenhar()


class TurbinaJogador(Animate):
    def __init__(self):
        self.sprite = SPRITES["boost"]
        super().__init__(self.sprite, DURACAO_DEFAULT)

    def desenha(self, x_jogador, y_jogador):
        pyxel.blt(x_jogador, y_jogador + 15, self.sprite.imagem, self.u_atual, self.sprite.v, self.sprite.largura, self.sprite.altura, 0)