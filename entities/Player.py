import sprites
import config

class Player:
    def __init__(self, name, life, velocity):
        self.name = name
        self.life = life
        self.velocity = velocity

        self.player_down = sprites.player_down
        self.player_up = sprites.player_up
        self.player_left = sprites.player_left
        self.player_right = sprites.player_right
        self.player_crushing = sprites.player_crushing
        self.player_falling = sprites.player_falling

        self.current_sprite = self.player_down

        self.size_jump_horizontal = self.player_right.width
        self.size_jump_vertical = self.player_up.height

        self.last_jump_time = 0
        self.jump_cooldown = 0.2

        self.screen_margin_x = (config.janela.largura % self.current_sprite.width) / 2
        self.screen_margin_y = (config.janela.altura % self.current_sprite.height) / 2

        self.player_x = config.janela.largura / 2 - self.current_sprite.width / 2
        self.player_y = config.janela.altura - self.current_sprite.height - self.screen_margin_y

        self.move_direction = None

        self.crushing = False
        self.falling = False
        self.reespawn_cd = 1
        self.reespawn_timer = 0



    def handle_input(self):
        if not self.crushing and not self.falling:
            if config.keyboard.key_down("UP") or config.keyboard.key_down("W"):
                self.move_direction = "up"
            elif config.keyboard.key_down("DOWN") or config.keyboard.key_down("S"):
                self.move_direction = "down"
            elif config.keyboard.key_down("LEFT") or config.keyboard.key_down("A"):
                self.move_direction = "left"
            elif config.keyboard.key_down("RIGHT") or config.keyboard.key_down("D"):
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

        self.last_jump_time = current_time
        self.move_direction = None

    def update(self):
        self.current_sprite.set_position(self.player_x, self.player_y)
        self.current_sprite.update()

    def draw(self):
        self.current_sprite.draw()

    def limitar_bordas(self):

        if self.player_x <= self.screen_margin_x:
            self.player_x = self.screen_margin_x

        if self.player_y <= self.screen_margin_y:
            self.player_y = self.screen_margin_y

        if self.player_x + self.current_sprite.width >= config.janela.largura - self.screen_margin_x:
            self.player_x = config.janela.largura - self.current_sprite.width - self.screen_margin_x

        if self.player_y + self.current_sprite.height >= config.janela.altura - self.screen_margin_y:
            self.player_y = config.janela.altura - self.current_sprite.height - self.screen_margin_y

    def volta_pro_inicio(self):
        self.player_x = config.janela.largura / 2 - self.current_sprite.width / 2
        self.player_y = config.janela.altura - self.current_sprite.height - self.screen_margin_y
        self.current_sprite = self.player_down

    def check_atropelamento(self, carros):
        if not self.crushing and not self.falling:
            for carro in carros.carros:
                #Checagem apenas se o player se encontra na rua do carro
                if carro.y + carro.sprite.height/2 >= self.player_y and carro.y + carro.sprite.height/2 <= self.player_y + self.current_sprite.height:
                    if self.current_sprite.collided(carro.sprite):
                        self.current_sprite = self.player_crushing
                        self.current_sprite.set_curr_frame(0)
                        self.crushing = True
        
        if self.crushing:
            if self.current_sprite.get_curr_frame() == 3:
                self.crushing = False
                self.volta_pro_inicio()

    def caiu_morreu(self, buracos):
        if not self.falling and not self.crushing:
            for buraco in buracos:
                if buraco.y > self.player_y and (self.player_x + self.current_sprite.width/2 > buraco.x and self.player_x < buraco.x + buraco.sprite.width - self.current_sprite.width/2):
                    if self.current_sprite.collided(buraco.sprite):
                        self.player_y = buraco.y - self.current_sprite.height/2
                        self.player_x = buraco.x
                        self.current_sprite = self.player_falling
                        self.current_sprite.set_curr_frame(0)
                        self.falling = True
        
        if self.falling:
            if self.current_sprite.get_curr_frame() == 4:
                self.falling = False
                self.volta_pro_inicio()