import math
import pyxel
import random

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

    def update(self):
        if random.uniform(0, 1) > PARTICLE_SPAWN_PERCENTAGE:  # 40% de chance de spawnar particula
            self.particulas.append(Particula.fromRandom())

        for particula in self.particulas:
            particula.update()
        
        self.__limpa_particulas()
        
    
    @staticmethod
    def __background():
        pyxel.rect(0, 0, pyxel.width, pyxel.height, pyxel.COLOR_BLACK)

    def __limpa_particulas(self):
        if self.particulas and self.particulas[0].y >= pyxel.height:  # Se houver pelo menos uma particula e a primeira da lista já passou da tela, elimina ela.
            self.particulas.pop(0)  

    def draw(self):
        Cena.__background()
        for particula in self.particulas:
            particula.draw()