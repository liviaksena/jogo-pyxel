import math
import pyxel
import random
from enum import Enum

from src.sprite import SPRITES

class EstadoCena(Enum):
    JOGANDO = 1
    BOSS = 2
    GAME_OVER = 3
    WIN = 4
    


SCREEN_OFFSET = 5
PARTICLE_SPAWN_PERCENTAGE = 0.4

class Particula:
    def __init__(self, x: int, velocidade: float):
        self.x = x
        self.y = - 30
        self.velocidade = velocidade
        self.dt = 0  # delta_time

    def update(self):
        self.y += math.e ** (self.dt * self.velocidade)
        self.dt += 1

    def draw(self):
        pyxel.rect(self.x, self.y, 1, 1, pyxel.COLOR_WHITE)

    @staticmethod
    def fromRandom(): 
        return Particula(x = random.uniform(0 + SCREEN_OFFSET, pyxel.width - SCREEN_OFFSET), velocidade = 0.1)
        

class Cena:
    def __init__(self):
        self.particulas = []
        self.estado = EstadoCena.JOGANDO 
    def update(self):
        if self.estado == EstadoCena.JOGANDO:
            if random.uniform(0, 1) > PARTICLE_SPAWN_PERCENTAGE:  # 40% de chance de spawnar particula
                self.particulas.append(Particula.fromRandom())

            for particula in self.particulas:
                particula.update()
        
        self.__limpa_particulas()
        

    def __limpa_particulas(self):
        if self.particulas and self.particulas[0].y >= pyxel.height:  # Se houver pelo menos uma particula e a primeira da lista já passou da tela, elimina ela.
            self.particulas.pop(0)  

    def draw(self,hp=0, pontuacao=0):

        if self.estado == EstadoCena.GAME_OVER:
            pyxel.text(60, 70, "GAME OVER", pyxel.COLOR_RED)
            pyxel.text(30, 80, "Pressione R para reiniciar", pyxel.frame_count % 16)
        elif self.estado == EstadoCena.WIN:
            pyxel.text(60, 70, "YOU WIN", pyxel.COLOR_GREEN)
            pyxel.text(30, 80, "Pressione R para reiniciar", pyxel.frame_count % 16)
        else:
            self.desenha_vida(hp=hp/5) 
            self.desenha_pontuacao(pontuacao=pontuacao) 
            for particula in self.particulas:
                particula.draw()

    def desenha_vida(self,hp):
        pc = SPRITES["player-card"]
        y = pyxel.height - pc.altura
        pyxel.blt(0, y, pc.imagem, pc.u, pc.v, pc.largura, pc.altura)
        pyxel.rect(x = 26, y = y + 3, w = 50 * hp, h = 3, col= pyxel.COLOR_RED)

    def desenha_pontuacao(self, pontuacao):    
        pc = SPRITES["player-card"]
        y = pyxel.height - pc.altura
        pyxel.text(30, y + 17,f"{pontuacao}", col = pyxel.COLOR_PINK)
        