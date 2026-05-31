import random

from PPlay.sound import Music
import config
import sprites
from entities import Player, CarSpawner, Buraco

def jogo():
    musica = Music('sounds/The_Rush_at_Avenida.mp3')
    musica.play()
    car_spawner1 = CarSpawner.CarSpawner(0, 230, 'left')
    car_spawner2 = CarSpawner.CarSpawner(0, 330, 'left')
    car_spawner3 = CarSpawner.CarSpawner(config.janela.largura, 570, 'right')
    car_spawner4 = CarSpawner.CarSpawner(config.janela.largura, 690, 'right')

    buracos = Buraco.buraco_generator(3)
    player = Player.Player("Player1", 3, 100)
    tempo = 0
    while True:

        config.janela.clear()
        sprites.background_game.draw()

        dt = config.janela.delta_time()
        tempo += dt

        if config.keyboard.key_pressed("ESC"):
            config.Tela = "Menu"
            return
        

        Buraco.buraco_drawer(buracos)

        player.check_atropelamento(car_spawner1)
        player.check_atropelamento(car_spawner2)
        player.check_atropelamento(car_spawner3)
        player.check_atropelamento(car_spawner4)
        player.caiu_morreu(buracos)
        player.handle_input()
        player.move(tempo)
        player.update()
        player.draw()


        car_spawner1.loop()
        car_spawner2.loop()
        car_spawner3.loop()
        car_spawner4.loop()

