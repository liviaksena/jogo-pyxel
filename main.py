import pyxel

class Jogo:
    def __init__(self):
        pyxel.init(160, 120, title="Meu Jogo Pyxel")
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)


Jogo()