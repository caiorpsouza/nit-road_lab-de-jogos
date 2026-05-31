import config
import sprites
from entities import Player

def jogo():

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

        player.move(tempo)
        player.update()
        player.draw()


