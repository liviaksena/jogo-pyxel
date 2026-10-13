from dataclasses import dataclass


DURACAO_DEFAULT = 24

@dataclass(frozen=True)
class Sprite:
    imagem: int # índice da imagem no Pyxel
    u: int # coordenada x do sprite na imagem
    v: int # coordenada y do sprite na imagem
    largura: int # largura do sprite na imagem
    altura: int # altura do sprite na imagem
    n_quadros: int = 1 # numero de quadros para reproduzir a animacao



SPRITES: dict[str, Sprite] = {
    "jogador": Sprite(imagem=0, u=16, v=0, largura=16, altura=16),
    "boost": Sprite(imagem=0, u=48, v=0, largura=16, altura=16, n_quadros=2),
    "projetil": Sprite(imagem=0, u=80, v=0, largura=16, altura=16),
    "explosao": Sprite(imagem=0, u=96, v=0, largura=16, altura=16, n_quadros=6),
    "inimigo1": Sprite(imagem=0, u=0, v=16, largura=16, altura=16, n_quadros=5),
    "inimigo2": Sprite(imagem=0, u=144, v=16, largura=16, altura=16, n_quadros=5),
    "boss": Sprite(imagem=0, u=0, v=48, largura=54, altura=64, n_quadros=2),
    "projetil-boss": Sprite(imagem=0, u=96, v=128, largura=16, altura=32),

    ## UI
    "player-card": Sprite(imagem=1, u=0, v=0, largura=80, altura=28),
    "play-button": Sprite(imagem=1, u=183, v=50, largura=55, altura=15),
    "exit-button": Sprite(imagem=1, u=183, v=90, largura=55, altura=15),
}