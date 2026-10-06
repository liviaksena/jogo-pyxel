import pyxel
from src.cena import Cena
from src.jogador import Jogador
from src.inimigo import GerenciaInimigos, Inimigo


class Jogo:
    def __init__(self):
        pyxel.init(160, 120, fps=60,title="SkyFall")
        self.cena = Cena()
        self.jogador = Jogador()
        self.gerencia_inimigos = GerenciaInimigos()

        pyxel.run(self.update, self.draw)

    def update(self):
        self.jogador.atualizar()
        self.cena.update()
        self.gerencia_inimigos.atualizar_inimigos()
        self.gerar_inimigos()

        for tiro in self.jogador.tiros:
            for inimigo in self.gerencia_inimigos.inimigos:
                if self.verificar_colisao(tiro, inimigo):
                    self.jogador.tiros.remove(tiro)
                    self.gerencia_inimigos.inimigos.remove(inimigo)
                    break

    def draw(self):
        pyxel.cls(0)
        self.cena.draw()
        self.jogador.desenhar()

        for inimigo in self.gerencia_inimigos.inimigos:
            inimigo.desenhar()

    def verificar_colisao(self, obj1, obj2):
        if (
            obj1.x < obj2.x + obj2.largura
            and obj1.x + obj1.largura > obj2.x
            and obj1.y < obj2.y + obj2.altura
            and obj1.y + obj1.altura > obj2.y
        ):
            return True
        return False

    def gerar_inimigos(self):
        if pyxel.frame_count % 60 == 0:
            x = pyxel.rndi(0, 160 - 10)
            y = -10
            inimigo = Inimigo(x, y)
            self.gerencia_inimigos.adicionar_inimigo(inimigo)