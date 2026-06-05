class Prop:
    def __init__(self, sprite, x, y, speed, loop, lane):
        self.lane = lane
        self.sprite = sprite
        self.x = x
        self.y = y
        self.last_dx = 0
        self.last_dy = 0
        self.speed = speed
        self.sprite.set_total_duration(loop)
        self.sprite.set_position(x, y)
    
    def set_position(self, x, y):
        self.sprite.set_position(x, y)
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.last_dx = dx
        self.last_dy = dy
        self.x += dx
        self.y += dy
        self.sprite.set_position(self.x, self.y)


    def draw(self):
        self.sprite.update()
        self.sprite.draw()