import sprites
import config
import sounds

class Player:
    def __init__(self, name, life, velocity):
        self.name = name
        self.life = life
        self.velocity = velocity

        self.player_down = sprites.player_down
        self.player_up = sprites.player_up
        self.player_left = sprites.player_left
        self.player_right = sprites.player_right

        self.current_sprite = self.player_down

        self.size_jump_horizontal = self.player_right.width
        self.size_jump_vertical = self.player_up.height

        self.last_jump_time = 0
        self.jump_cooldown = 0.2

        self.player_x = config.janela.largura / 2 - self.current_sprite.width / 2
        self.player_y = config.janela.altura - self.current_sprite.height - 50

        self.move_direction = None

        self.jump_sound = sounds.jump_sound

    def handle_input(self):
        if config.keyboard.key_down("UP"):
            self.move_direction = "up"
        elif config.keyboard.key_down("DOWN"):
            self.move_direction = "down"
        elif config.keyboard.key_down("LEFT"):
            self.move_direction = "left"
        elif config.keyboard.key_down("RIGHT"):
            self.move_direction = "right"

    def move(self, current_time):

        if not self.move_direction:
            return

        if (current_time - self.last_jump_time) < self.jump_cooldown:
            return

        movements = {
            "up": (0, -self.size_jump_vertical, self.player_up),
            "down": (0, self.size_jump_vertical, self.player_down),
            "left": (-self.size_jump_horizontal, 0, self.player_left),
            "right": (self.size_jump_horizontal, 0, self.player_right),
        }

        dx, dy, sprite = movements[self.move_direction]

        self.player_x += dx
        self.player_y += dy
        self.current_sprite = sprite

        self.limitar_bordas()

        self.current_sprite.set_curr_frame(0)
        self.current_sprite.play()
        self.jump_sound.play()

        self.last_jump_time = current_time
        self.move_direction = None

    def update(self):
        self.current_sprite.set_position(self.player_x, self.player_y)
        self.current_sprite.update()

    def draw(self):
        self.current_sprite.draw()

    def limitar_bordas(self):

        if self.player_x < 0:
            self.player_x = 0

        if self.player_y < 0:
            self.player_y = 0

        if self.player_x + self.current_sprite.width > config.janela.largura:
            self.player_x = config.janela.largura - self.current_sprite.width

        if self.player_y + self.current_sprite.height > config.janela.altura:
            self.player_y = config.janela.altura - self.current_sprite.height