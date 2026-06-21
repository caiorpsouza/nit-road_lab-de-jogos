import random

from PPlay import sprite
import sprites
from assets import resource_path


class Buraco:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = sprite.Sprite(resource_path("images/obstacles/buraco.png"))
        self.sprite.set_position(self.x, self.y)

    def draw(self):
        self.sprite.draw()

def buraco_generator(num_de_buracos):
    buracos = []
    for _ in range(num_de_buracos):
        novo_buraco = Buraco(sprites.buraco.width * random.randint(6, 14), (sprites.fase1.height/16 * random.randint(5,12))+10)
        buracos.append(novo_buraco)
    
    return buracos

def buraco_drawer(buracos):
    for buraco in buracos:
        buraco.draw()