import pyxel
from src.cena import Cena, EstadoCena
from src.jogador import Jogador
from src.inimigo import Boss, GerenciaInimigos, Inimigo


class Jogo:
    def __init__(self):
        pyxel.init(180, 180, fps=60,title="SkyFall")
        pyxel.load("../jogo-pyxel.pyxres")
        self.cena = Cena()
        self.jogador = Jogador()
        self.gerencia_inimigos = GerenciaInimigos()
        self.vida_jogador = 5
        self.pontuacao = 0

    

        pyxel.run(self.update, self.draw)

    def update(self):
        if self.cena.estado == EstadoCena.JOGANDO:
            self.jogador.atualizar()
            self.cena.update()
            self.gerencia_inimigos.atualizar_inimigos()
            self.gerar_inimigos()

            for tiro in self.jogador.tiros:
                        for inimigo in self.gerencia_inimigos.inimigos:
                            if self.verificar_colisao(tiro, inimigo):
                                self.gerencia_inimigos.inimigos.remove(inimigo) 
                                self.pontuacao += 1
                                self.jogador.tiros.remove(tiro)
                                break
            
            for inimigo in self.gerencia_inimigos.inimigos:
                if self.verificar_colisao(self.jogador, inimigo):
                    self.gerencia_inimigos.inimigos.remove(inimigo)
                    self.vida_jogador -= 1
    
                    if self.vida_jogador <= 0:
                        self.vida_jogador = 0
                        self.cena.estado = EstadoCena.GAME_OVER
                        break
            if self.pontuacao >=5:
                self.cena.estado = EstadoCena.BOSS
                self.boss = Boss()

        elif self.cena.estado == EstadoCena.BOSS:
            self.jogador.atualizar()
            self.cena.update()
            self.boss.atualizar(self.jogador)

            for tiro in self.jogador.tiros:
                if self.verificar_colisao(tiro, self.boss):
                    self.boss.vida -= 1
                    self.jogador.tiros.remove(tiro)
                    if self.boss.vida <= 0:
                        self.cena.estado = EstadoCena.WIN
                        break      

            for tiro in self.jogador.tiros:
                for projetil in self.boss.projeteis:
                    if self.verificar_colisao(tiro, projetil):
                        self.jogador.tiros.remove(tiro)
                        self.boss.projeteis.remove(projetil)
                        break

            for projetil in self.boss.projeteis:
                if self.verificar_colisao(self.jogador, projetil):
                    self.boss.projeteis.remove(projetil)
                    self.vida_jogador -= 1
                    if self.vida_jogador <= 0:
                        self.vida_jogador = 0
                        self.cena.estado = EstadoCena.GAME_OVER
                        break

        elif self.cena.estado == EstadoCena.GAME_OVER:
            if pyxel.btnp(pyxel.KEY_R):
                self.reiniciar_jogo()


            return
        
    def reiniciar_jogo(self):
        self.cena.estado = EstadoCena.JOGANDO
        self.jogador = Jogador()
        self.gerencia_inimigos = GerenciaInimigos()
        self.vida_jogador = 5
        self.pontuacao = 0

    def draw(self):
        pyxel.cls(0)
        self.cena.draw(hp=self.vida_jogador, pontuacao=self.pontuacao)
        self.jogador.desenhar()

        for inimigo in self.gerencia_inimigos.inimigos:
            inimigo.desenhar()

        if self.cena.estado == EstadoCena.BOSS:
            self.boss.desenhar()

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
