import pyxel

from src.sprite import Sprite


class Animate:
    """classe para animar os sprites"""
    def __init__(self, sprite: Sprite, duracao: int):
        self.sprite  = sprite
        self.duracao = duracao # ticks
        self.indice   = 0

    def atualiza_animacao(self):
        if pyxel.frame_count % self.duracao == 0:
            if self.indice + 1 >= self.sprite.n_quadros:
                self.indice = 0
            else:
                self.indice += 1

    @property
    def u_atual(self):
        deslocamento = self.indice * self.sprite.largura
        return self.sprite.u + deslocamento