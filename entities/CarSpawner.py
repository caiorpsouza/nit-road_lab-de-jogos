from PPlay import sprite
import config
from entities.Carro import Carro
import sprites
import random

class CarSpawner:
    def __init__(self, lane, side, vehicles_types, velocity):
        self.lane = lane
        self.carros = []
        self.car_speed = velocity
        self.side = side
        self.vehicles_types = vehicles_types
        self.spawn_clearance = max(sprites.VEHICLES[tipo].width for tipo in self.vehicles_types)

        self.spawn_cooldown = self._next_spawn_cooldown()
        self.spawn_timer = 5
        # Comentando pois já tem o spawn_cooldown
        # self.spawn_margin = random.randint(-10, 10) / 100

        if self.side == 'right':
            self.x = config.janela.largura
        else:
            self.x = 0

        self.y = sprites.fase1.height / 16 * (self.lane - 1)

    def _next_spawn_cooldown(self):
        return random.randint(30, 55) / 10

    def _pode_spawnar(self):
        if self.side == 'right':
            return all(carro.sprite.x + carro.sprite.width <= config.janela.largura - self.spawn_clearance for carro in self.carros)

        return all(carro.sprite.x >= self.spawn_clearance for carro in self.carros)
    

    def loop(self):
        self.spawn_timer += config.janela.delta_time()
        if self.spawn_timer >= self.spawn_cooldown and self._pode_spawnar():
            self.spawn_cooldown = self._next_spawn_cooldown()
            self.spawn_timer = 0

            veiculo_escolhido = random.choice(self.vehicles_types)
            self.spawnVehicle(veiculo_escolhido)

        for carro in self.carros:
            if carro.sprite.x > config.janela.largura:
                self.carros.remove(carro)
            if carro.sprite.y > config.janela.altura:
                self.carros.remove(carro)
            if carro.sprite.x + carro.sprite.width < 0:
                self.carros.remove(carro)
            if carro.sprite.y + carro.sprite.height < 0:
                self.carros.remove(carro)

            if self.side == 'right':
                carro.sprite.x -= carro.speed * config.janela.delta_time()
            else:
                carro.sprite.x += carro.speed * config.janela.delta_time()
            carro.sprite.update()

    def draw(self):
        for carro in self.carros:
            carro.sprite.draw()

    def spawnVehicle(self, tipo):
        sprite_ref = sprites.VEHICLES[tipo]
        if self.side == 'right':
            novo_carro = Carro(
                sprite.Sprite(f'images/vehicles/{tipo}_right.png', 2),
                self.x,
                self.y - sprite_ref.height / 2,
                self.car_speed,
                500
            )

            novo_carro.sprite.set_position(
                novo_carro.x,
                self.y - sprite_ref.height / 2
            )

        else:
            novo_carro = Carro(
                sprite.Sprite(f'images/vehicles/{tipo}_left.png', 2),
                self.x,
                self.y - sprite_ref.height / 2,
                self.car_speed,
                500
            )

            novo_carro.sprite.set_position(
                novo_carro.x - sprite_ref.width,
                self.y - sprite_ref.height / 2
            )

        self.carros.append(novo_carro)
