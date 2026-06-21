from PPlay import *
import config
import sounds
import sprites

def play():
    # Textos da tela de vitória
    titulo = sprite.Sprite("images/title/game_over.png")
    titulo.set_position(config.janela.largura/2 - titulo.width/2, 150)
    sounds.parar_game()
    sounds.death_music.play()
    while True:
        if config.janela.keyboard.key_down('ESC'):
            config.Tela = 'Menu'
            sounds.death_music.stop()
            return 0
        # Desenhar
        sprites.background_death.draw()
        titulo.draw()
        
        config.janela.update()
