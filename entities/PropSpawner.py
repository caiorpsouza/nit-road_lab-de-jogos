import random

from PPlay import sprite
import config
from entities.Prop import Prop
import sprites


class PropSpawner:
    def __init__(self, lane, side, prop_types, velocity):
        self.lane = lane
        self.props = []
        self.prop_speed = velocity
        self.side = side
        self.prop_types = prop_types
        self.spawn_clearance = max(sprites.PROPS[tipo].width for tipo in self.prop_types)

        self.spawn_cooldown = self._next_spawn_cooldown()
        self.spawn_timer = 5
        

        if self.side == 'right':
            self.x = config.janela.largura
        else:
            self.x = 0

        self.y = sprites.fase1.height / 16 * (self.lane - 1)

    def _next_spawn_cooldown(self):
        return random.randint(30, 55) / 10

    def _pode_spawnar(self):
        if self.side == 'right':
            return all(prop.sprite.x + prop.sprite.width <= config.janela.largura - self.spawn_clearance for prop in self.props)

        return all(prop.sprite.x >= self.spawn_clearance for prop in self.props)
    
    def loop(self):
        print(self.props)
        self.spawn_timer += config.janela.delta_time()

        if self.spawn_timer >= self.spawn_cooldown and self._pode_spawnar():
            self.spawn_cooldown = self._next_spawn_cooldown()
            self.spawn_timer = 0

            prop_escolhido = random.choice(self.prop_types)
            self.spawnProp(prop_escolhido)

        for prop in self.props:
            if prop.sprite.x > config.janela.largura:
                self.props.remove(prop)
            if prop.sprite.y > config.janela.altura:
                self.props.remove(prop)
            if prop.sprite.x + prop.sprite.width < 0:
                self.props.remove(prop)
            if prop.sprite.y + prop.sprite.height < 0:
                self.props.remove(prop)

            if self.side == 'right':
                prop.sprite.x -= prop.speed * config.janela.delta_time()
            else:
                prop.sprite.x += prop.speed * config.janela.delta_time()
            prop.sprite.update()

    def draw(self):
        for prop in self.props:
            prop.sprite.draw()

    def spawnProp(self, tipo):
        sprite_ref = sprites.PROPS[tipo]
        novo_prop = Prop(
                        sprite.Sprite(f'images/props/{tipo}.png', 2),
                        self.x,
                        self.y - sprite_ref.height / 2,
                        self.prop_speed,
                        500
                    )
        if self.side == 'right':
            novo_prop.sprite.set_position(
                novo_prop.x,
                self.y - sprite_ref.height / 2
            )
        else:
            novo_prop.sprite.set_position(
                novo_prop.x - sprite_ref.width,
                self.y - sprite_ref.height / 2
            )

        self.props.append(novo_prop)