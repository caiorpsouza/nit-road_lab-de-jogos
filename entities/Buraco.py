import random

from PPlay import sprite
import sprites


class Buraco:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = sprite.Sprite("images/obstacles/buraco.png")
        self.sprite.set_position(self.x, self.y)

    def draw(self):
        self.sprite.draw()

def buraco_generator(num_de_buracos):
    buracos = []
    for _ in range(num_de_buracos):
        novo_buraco = Buraco(sprites.buraco.width * random.randint(2, 13), sprites.buraco.height * random.randint(2, 7))
        buracos.append(novo_buraco)
    
    return buracos

def buraco_drawer(buracos):
    for buraco in buracos:
        buraco.draw()