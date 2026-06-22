import fases
import sprites
import config
import sounds
from PPlay.collision import Collision

class Player:
    def __init__(self, name, lifes, velocity):
        self.name = name
        self.lifes = lifes
        self.velocity = velocity

        self.player_down = sprites.player_down
        self.player_up = sprites.player_up
        self.player_left = sprites.player_left
        self.player_right = sprites.player_right
        self.player_crushing = sprites.player_crushing
        self.player_falling = sprites.player_falling
        self.player_drowning = sprites.player_falling

        self.current_sprite = self.player_down

        self.size_jump_horizontal = self.player_right.width
        self.size_jump_vertical = self.player_up.height

        self.last_jump_time = 0
        self.jump_cooldown = 0.2

        self.jump_sound = sounds.sons["jump"]

        self.screen_margin_x = (config.janela.largura % self.current_sprite.width) / 2
        self.screen_margin_y = (config.janela.altura % self.current_sprite.height) / 2

        self.player_x = config.janela.largura / 2 - self.current_sprite.width / 2
        self.player_y = config.janela.altura - self.current_sprite.height - self.screen_margin_y

        self.move_direction = None

        self.crushing = False
        self.falling = False
        self.drowning = False
        self.reespawn_cd = 1
        self.reespawn_timer = 0

        self.current_prop = None
        self.just_landed_on_prop = False
        self.last_prop = None
        self.prop_fall_margin = 5
        self.car_hitbox_shrink_x = 0.5
        self.car_hitbox_shrink_y = 0.4

    def get_lane(self):
        fase = fases.phases[config.fase - 1]
        altura_lane = fase['background'].height / 16
        return round(self.player_y / altura_lane) + 1
    
    def retorna_vidas(self):
        return self.lifes

    def _shrunk_bounds(self, sprite, shrink_x=0.22, shrink_y=0.12):
        inset_x = sprite.width * shrink_x / 2
        inset_y = sprite.height * shrink_y / 2
        return (
            sprite.x + inset_x,
            sprite.y + inset_y,
            sprite.width - (inset_x * 2),
            sprite.height - (inset_y * 2),
        )

    def _bounds_overlap(self, bounds_a, bounds_b):
        ax, ay, aw, ah = bounds_a
        bx, by, bw, bh = bounds_b
        return (ax < bx + bw and
                ax + aw > bx and
                ay < by + bh and
                ay + ah > by)

    def handle_input(self):
        if not self.crushing and not self.falling and not self.drowning:
            if config.keyboard.key_pressed("UP") or config.keyboard.key_pressed("W"):
                self.move_direction = "up"
            elif config.keyboard.key_pressed("DOWN") or config.keyboard.key_pressed("S"):
                self.move_direction = "down"
            elif config.keyboard.key_pressed("LEFT") or config.keyboard.key_pressed("A"):
                self.move_direction = "left"
            elif config.keyboard.key_pressed("RIGHT") or config.keyboard.key_pressed("D"):
                self.move_direction = "right"

    def move(self, current_time):

        if (current_time - self.last_jump_time) < self.jump_cooldown:
            return

        self.handle_input()

        if not self.move_direction:
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
        if config.efeitos:
            self.jump_sound.play()

        # Se se moveu enquanto estava em um prop, marca para não aplicar follow_prop este frame
        if self.current_prop:
            self.just_landed_on_prop = True

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

        # Comentando para deixar o player ir para proxima fase
        # if self.player_y <= self.screen_margin_y:
        #     self.player_y = self.screen_margin_y

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
            player_bounds = self._shrunk_bounds(
                self.current_sprite,
                self.car_hitbox_shrink_x,
                self.car_hitbox_shrink_y,
            )
            for carro in carros.carros:
                carro_bounds = self._shrunk_bounds(
                    carro.sprite,
                    self.car_hitbox_shrink_x,
                    self.car_hitbox_shrink_y,
                )

                # Primeiro exige sobreposição de hitbox reduzida para evitar colisão em bordas vazias.
                if not self._bounds_overlap(player_bounds, carro_bounds):
                    continue

                if Collision.perfect_collision(self.current_sprite, carro.sprite):
                    self.current_sprite = self.player_crushing
                    self.current_sprite.set_curr_frame(0)
                    self.crushing = True
                    self.lifes -= 1

        if self.crushing:
            if self.current_sprite.get_curr_frame() == 3:
                self.crushing = False
                self.volta_pro_inicio()

    def caiu_morreu(self, buracos):
        if not self.falling and not self.crushing:
            for buraco in buracos:
                if buraco.y > self.player_y and (self.player_x + self.current_sprite.width/2 > buraco.x and self.player_x < buraco.x + buraco.sprite.width - self.current_sprite.width/2):
                    if self.current_sprite.collided(buraco.sprite):
                        self.player_y = buraco.y - buraco.sprite.height/3
                        self.player_x = buraco.x + buraco.sprite.width/3
                        self.current_sprite = self.player_falling
                        self.current_sprite.set_curr_frame(0)
                        self.falling = True
                        self.lifes -= 1
        
        if self.falling:
            if self.current_sprite.get_curr_frame() == 4:
                self.falling = False
                self.volta_pro_inicio()
    
    #A partir daqui é perigo...
    def check_afogamento(self):
        # Se está em um prop, cancela o afogamento!
        if self.current_prop is not None:
            if self.drowning:
                self.drowning = False
                self.current_sprite = self.player_down
                self.current_sprite.set_curr_frame(0)
            return
        
        if not self.drowning:
            fase = fases.phases[config.fase - 1]
            lane = self.get_lane()

            is_water = fase['terrains'][lane] == 'water'

            if not self.current_prop and is_water:
                self.current_sprite = self.player_drowning
                self.current_sprite.set_curr_frame(0)
                self.drowning = True
                
            
        if self.drowning:
            if self.current_sprite.get_curr_frame() == 4:
                self.drowning = False
                self.volta_pro_inicio()
                self.lifes -= 1
    
    def release_prop(self):
        self.last_prop = self.current_prop
        self.current_prop = None
        self.just_landed_on_prop = False

    def follow_prop(self):
        if self.current_prop is None:
            return

        self.player_x += self.current_prop.last_dx
        self.player_y += self.current_prop.last_dy
        self.current_sprite.set_position(self.player_x, self.player_y)

        #PROP LEVA O PLAYER PARA O FIM DA TELA
        if self.player_x + self.current_sprite.width >= config.janela.largura or self.player_x <= 0:
            self.volta_pro_inicio()
            self.lifes -= 1

    def _is_still_safely_on_prop(self):
        if self.current_prop is None:
            return False

        player_left = self.player_x
        player_right = self.player_x + self.current_sprite.width
        prop_left = self.current_prop.x
        prop_right = self.current_prop.x + self.current_prop.sprite.width
        overlap_left = max(player_left, prop_left)
        overlap_right = min(player_right, prop_right)
        overlap_width = overlap_right - overlap_left

        return overlap_width >= (self.current_sprite.width / 2) + self.prop_fall_margin


    def land_on_prop(self, prop):
        self.current_prop = prop
        self.just_landed_on_prop = True
        self.player_y = prop.y + prop.sprite.height / 2 - self.current_sprite.height
        # Mantém o alinhamento horizontal atual; só centraliza no eixo vertical do prop.
        self.current_sprite.set_position(self.player_x, self.player_y)

    def update_on_props(self, prop_spawners):
        if not self.current_prop:
            return
        
        # Ignora verificação de colisão no frame que pousou para evitar soltar prematuramente
        if self.just_landed_on_prop:
            self.just_landed_on_prop = False
            self.follow_prop()
            return

        props = [prop for spawner in prop_spawners for prop in spawner.props]
        if (
            self.current_prop not in props
            or not self.current_sprite.collided(self.current_prop.sprite)
            or (self.current_prop.lane != self.get_lane())
            or not self._is_still_safely_on_prop()
        ):
            self.release_prop()
        else:
            self.follow_prop()

    def try_land_on_props(self, prop_spawners):

        if self.current_prop or self.crushing or self.falling:
            return

        props = [prop for spawner in prop_spawners for prop in spawner.props]
        for prop in props:
            # Não deixa pousar no mesmo prop que acabou de sair
            if prop == self.last_prop:
                continue
            if self.get_lane() == prop.lane:
                if self.current_sprite.collided(prop.sprite):
                        self.land_on_prop(prop)
                        self.last_prop = None
                        break    
