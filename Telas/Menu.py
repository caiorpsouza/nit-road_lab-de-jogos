from PPlay import *
from PPlay.sound import Music
import config
import sprites

def play() :
    musica = Music('sounds/Brisa_na_Varanda.mp3')
    musica.play()
    while True:

        #Clique no botão Sair
        if (config.janela.mouse.button_down(1) and config.janela.mouse.is_over_object(sprites.quit_btn)):
            config.is_running = False
            return 0
        if (config.janela.mouse.button_down(1) and config.janela.mouse.is_over_object(sprites.diff_btn)):
            config.Tela = 'Dificuldade'
            return 0
        if (config.janela.mouse.button_down(1) and config.janela.mouse.is_over_object(sprites.play_btn)):
            config.Tela = 'Jogo'
            return 0

        sprites.background_menu.draw()
        sprites.title.draw()
        sprites.play_btn.draw()
        sprites.diff_btn.draw()
        sprites.scores_btn.draw()
        sprites.quit_btn.draw()

        config.janela.update()
