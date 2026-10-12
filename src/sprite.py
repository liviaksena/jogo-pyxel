from dataclasses import dataclass


@dataclass(frozen=True)
class Sprite:
    imagem: int # índice da imagem no Pyxel
    u: int # coordenada x do sprite na imagem
    v: int # coordenada y do sprite na imagem
    largura: int # largura do sprite na imagem
    altura: int # altura do sprite na imagem
    n_quadros: int = 1 # numero de quadros para reproduzir a animacao



SPRITES: dict[str, Sprite] = {
    "jogador": Sprite(imagem=0, u=0, v=0, largura=16, altura=16, n_quadros=3),
    "boost": Sprite(imagem=0, u=48, v=0, largura=16, altura=16, n_quadros=2),
    "projetil": Sprite(imagem=0, u=80, v=0, largura=16, altura=16),
    "explosao": Sprite(imagem=0, u=96, v=0, largura=16, altura=16, n_quadros=6),
    "inimigo1": Sprite(imagem=0, u=0, v=16, largura=16, altura=16, n_quadros=5),
    "inimigo2": Sprite(imagem=0, u=80, v=16, largura=16, altura=16, n_quadros=5),

    ## UI
    "player-card": Sprite(imagem=1, u=0, v=0, largura=80, altura=28),
}