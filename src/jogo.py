import pyxel

from src.jogador import Jogador
from src.inimigo import Inimigo


class Jogo:
    def __init__(self):
        pyxel.init(160, 120, title="SkyFall")

        self.jogador = Jogador()
        self.inimigo = Inimigo(75, 10)

        pyxel.run(self.update, self.draw)

    def update(self):
        self.jogador.atualizar()
        self.inimigo.atualizar()

    def draw(self):
        pyxel.cls(0)

        self.jogador.desenhar()
        self.inimigo.desenhar()