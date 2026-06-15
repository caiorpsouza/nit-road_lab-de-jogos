import config
import sprites


class LifeDisplay:
    def __init__(self):
        self.lifes = config.max_vidas
        self.vida_sprite = sprites.life
        self.lifes_perdidas = 0
        self.y = 0
        self.x = config.janela.largura


    def loop(self):
        for i in range(self.lifes):
            nova_vida = self.vida_sprite
            nova_vida.set_position(self.x - (i * (self.vida_sprite.width * 3/4)) - self.vida_sprite.width, 20)
            nova_vida.draw()


