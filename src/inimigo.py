import heapq
import math
import pyxel
import random
from enum import Enum
from src.animation import Animate
from src.sprite import DURACAO_DEFAULT, SPRITES

X_OFFSET = 10

class Side(Enum):
    ESQUERDA = -1
    DIREITA  =  1

class Inimigo(Animate):
    def __init__(self, x, y, tipo):
        self.x_origem = x
        self.x = x
        self.y = y
        self.y_origem = y
        self.deslocamento_y = 0
        self.tipo = tipo # tipo de inimigo 0 ou 1 (A ou B)
        self.side = Side.ESQUERDA
        if self.tipo == 0:
            self.sprite = SPRITES["inimigo1"]
        else:
            self.sprite = SPRITES["inimigo2"]
        self.largura = self.sprite.largura
        self.altura = self.sprite.altura
        self.velocidade = 1.5
        self.raio_circular = 16
        self.angulo = random.uniform(0, math.tau)
        self.velocidade_angular = 0.08
        super().__init__(self.sprite, DURACAO_DEFAULT)
        

    def atualizar(self):
        self.atualiza_animacao()


        if self.tipo == 0: # Comportamento do inimigo 1
            if self.x >= self.x_origem + X_OFFSET:
                self.side = Side.ESQUERDA
            elif self.x <= self.x_origem - X_OFFSET:
                self.side = Side.DIREITA
            self.x += 1 * self.side.value
            self.y += self.velocidade

        if self.tipo == 1: # Comportamento do inimigo 2
            self.angulo += self.velocidade_angular
            self.deslocamento_y += self.velocidade
            centro_y = self.y_origem + self.deslocamento_y
            self.x = self.x_origem + math.cos(self.angulo) * self.raio_circular
            self.y = centro_y + math.sin(self.angulo) * self.raio_circular
        

    def desenhar(self):
        pyxel.blt(self.x, self.y, self.sprite.imagem, self.u_atual, self.sprite.v, self.sprite.largura, self.sprite.altura, colkey=0)

class GerenciaInimigos:
    def __init__(self):
        self.inimigos = []

    def adicionar_inimigo(self, inimigo):
        self.inimigos.append(inimigo)

    def atualizar_inimigos(self):
        for inimigo in self.inimigos[:]:
            inimigo.atualizar()
            if inimigo.y > pyxel.height:
                self.inimigos.remove(inimigo)




### Implementação do Algoritmo A*, algoritmo de busca de menor caminho
### Foi utilizado IA para auxilio da implementação desse algoritmo
 
TAMANHO_GRADE = 16


def encontrar_caminho_a_estrela(inicio, destino, colunas, linhas):
    def heuristica(celula):
        return abs(celula[0] - destino[0]) + abs(celula[1] - destino[1])

    fila = [(heuristica(inicio), 0, inicio)]
    custos = {inicio: 0}
    anteriores = {}

    while fila:
        _, custo_atual, atual = heapq.heappop(fila)
        if custo_atual != custos[atual]:
            continue

        if atual == destino:
            caminho = [atual]
            while atual in anteriores:
                atual = anteriores[atual]
                caminho.append(atual)
            return caminho[::-1]

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            vizinho = (atual[0] + dx, atual[1] + dy)
            if not (0 <= vizinho[0] < colunas and 0 <= vizinho[1] < linhas):
                continue

            novo_custo = custo_atual + 1
            if novo_custo < custos.get(vizinho, float("inf")):
                custos[vizinho] = novo_custo
                anteriores[vizinho] = atual
                heapq.heappush(
                    fila,
                    (novo_custo + heuristica(vizinho), novo_custo, vizinho),
                )

    return [inicio]


class ProjetilBoss:
    def __init__(self, x, y):
        self.sprite = SPRITES["projetil-boss"] 
        self.x = float(x)
        self.y = float(y)
        self.largura = self.sprite.largura
        self.altura = self.sprite.altura
        self.velocidade = 0.75

    def atualizar(self, jogador):
        colunas = (pyxel.width + TAMANHO_GRADE - 1) // TAMANHO_GRADE
        linhas = (pyxel.height + TAMANHO_GRADE - 1) // TAMANHO_GRADE
        centro_x = self.x + self.largura / 2
        centro_y = self.y + self.altura / 2
        alvo_x = jogador.x + jogador.largura / 2
        alvo_y = jogador.y + jogador.altura / 2

        inicio = (
            min(int(centro_x // TAMANHO_GRADE), colunas - 1),
            min(int(centro_y // TAMANHO_GRADE), linhas - 1),
        )
        destino = (
            min(int(alvo_x // TAMANHO_GRADE), colunas - 1),
            min(int(alvo_y // TAMANHO_GRADE), linhas - 1),
        )
        caminho = encontrar_caminho_a_estrela(inicio, destino, colunas, linhas)

        if len(caminho) > 1:
            proxima_celula = caminho[1]
            ponto_x = (proxima_celula[0] + 0.5) * TAMANHO_GRADE
            ponto_y = (proxima_celula[1] + 0.5) * TAMANHO_GRADE
        else:
            ponto_x = alvo_x
            ponto_y = alvo_y

        dx = ponto_x - centro_x
        dy = ponto_y - centro_y
        distancia = math.hypot(dx, dy)
        if distancia <= self.velocidade:
            self.x += dx
            self.y += dy
        elif distancia:
            self.x += dx / distancia * self.velocidade
            self.y += dy / distancia * self.velocidade

    def desenhar(self):
        pyxel.blt(
            int(self.x),
            int(self.y),
            self.sprite.imagem,
            self.sprite.u,
            self.sprite.v,
            self.sprite.largura,
            self.sprite.altura,
            colkey=0,
        )


class Boss(Animate):
    def __init__(self, x=None, y=8):
        self.sprite = SPRITES["boss"]
        self.x = (pyxel.width - self.sprite.largura) // 2 if x is None else x
        self.y = y
        self.largura = self.sprite.largura
        self.altura = self.sprite.altura
        self.projeteis = []
        self.tempo_disparo = 0
        self.intervalo_disparo = 30
        self.vida = 30
        super().__init__(self.sprite, DURACAO_DEFAULT)

    def atualizar(self, jogador):
        self.atualiza_animacao()
        self.tempo_disparo += 1
        if self.tempo_disparo >= self.intervalo_disparo:
            self.atirar()
            self.tempo_disparo = 0

        for projetil in self.projeteis[:]:
            projetil.atualizar(jogador)
            if projetil.y > pyxel.height:
                self.projeteis.remove(projetil)

    def desenhar(self, side = 1):
        pyxel.rect(x = self.x + 3, y = self.y - 5, w = 50 * (self.vida / 30), h = 3, col= pyxel.COLOR_RED)
        pyxel.blt(self.x, self.y, self.sprite.imagem, self.u_atual, self.sprite.v, side * self.sprite.largura, self.sprite.altura, colkey=0)
        for projetil in self.projeteis:
            projetil.desenhar()

    def atirar(self):
        side = random.choice([0, 1])
        if side == 0:
            x = pyxel.rndi(15, self.x - 2)
        else:
            x = pyxel.rndi(self.x + self.sprite.largura, pyxel.width - 15)
        y = pyxel.rndi(int(self.y + (self.altura / 3)), self.y + self.altura)
        self.projeteis.append(ProjetilBoss(x, y))
