from PPlay import sprite
import config
from entities.Carro import Carro
import sprites
import random

class CarSpawner:
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.carros = []
        self.car_speed = 500
        self.side = side


        self.spawn_cooldown = random.randint(10,20)/10
        self.spawn_timer = 0
        self.spawn_margin = random.randint(-25, 25) / 100



    def loop(self):
        self.spawn_timer += config.janela.delta_time()

        if self.spawn_timer >= self.spawn_cooldown + self.spawn_margin:
            self.spawn_margin = random.randint(-25, 25) / 100
            self.spawn_cooldown = random.randint(10,20) / 10
            self.spawn_timer = 0
            carroEscolhido = random.randint(0,2)
            if carroEscolhido == 0:
                self.spawnRedCar()
            elif carroEscolhido == 1:
                self.spawnPoliceCar()
            elif carroEscolhido == 2:
                self.spawnYellowCar()

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
            carro.sprite.draw()

    def spawnRedCar(self):
        if self.side == 'right':
            novo_carro = Carro(sprite.Sprite('images/obstacles/red_car_right.png', 2), self.x, self.y - sprites.red_car.height/2, random.randint(500, 800))
            novo_carro.sprite.set_position(novo_carro.x, self.y - sprites.red_car.height/2)
        else:
            novo_carro =Carro(sprite.Sprite('images/obstacles/red_car_left.png', 2), self.x, self.y - sprites.red_car.height/2, random.randint(500, 800))
            novo_carro.sprite.set_position(novo_carro.x - sprites.red_car.width, self.y - sprites.red_car.height/2)
        self.carros.append(novo_carro)

    def spawnYellowCar(self):
        if self.side == 'right':
            novo_carro = Carro(sprite.Sprite('images/obstacles/yellow_car_right.png', 2), self.x, self.y - sprites.yellow_car.height/2, random.randint(500, 800))
            novo_carro.sprite.set_position(novo_carro.x, self.y - sprites.yellow_car.height/2)
        else:
            novo_carro =Carro(sprite.Sprite('images/obstacles/yellow_car_left.png', 2), self.x, self.y - sprites.yellow_car.height/2, random.randint(500, 800))
            novo_carro.sprite.set_position(novo_carro.x - sprites.yellow_car.width, self.y - sprites.yellow_car.height/2)
        self.carros.append(novo_carro)
    
    def spawnPoliceCar(self):
        if self.side == 'right':
            novo_carro = Carro(sprite.Sprite('images/obstacles/police_car_right.png', 2), self.x, self.y - sprites.police_car.height/2, random.randint(500, 800))
            novo_carro.sprite.set_position(novo_carro.x, self.y - sprites.police_car.height/2)
        else:
            novo_carro =Carro(sprite.Sprite('images/obstacles/police_car_left.png', 2), self.x, self.y - sprites.police_car.height/2, random.randint(500, 800))
            novo_carro.sprite.set_position(novo_carro.x - sprites.police_car.width, self.y - sprites.police_car.height/2)
        self.carros.append(novo_carro)

