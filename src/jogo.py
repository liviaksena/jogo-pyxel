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

        if self.inimigo is not None:
            self.inimigo.atualizar()

            for tiro in self.jogador.tiros[:]:
                if self.verificar_colisao(tiro, self.inimigo):
                    self.jogador.tiros.remove(tiro)
                    self.inimigo = None
                    break

    def draw(self):
        pyxel.cls(0)

        self.jogador.desenhar()

        if self.inimigo is not None:
            self.inimigo.desenhar()

    def verificar_colisao(self, obj1, obj2):
        if (
            obj1.x < obj2.x + obj2.largura
            and obj1.x + obj1.largura > obj2.x
            and obj1.y < obj2.y + obj2.altura
            and obj1.y + obj1.altura > obj2.y
        ):
            return True
        return False
