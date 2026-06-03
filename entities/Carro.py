
class Carro:
    def __init__(self, sprite, x, y, speed, loop):
        self.sprite = sprite
        self.x = x
        self.y = y
        self.speed= speed

        self.sprite.set_total_duration(loop)
    
    def set_position(self, x, y):
        self.sprite.set_position(x, y)
        self.x = x
        self.y = y

    def draw(self):
        self.sprite.update()
        self.sprite.draw()