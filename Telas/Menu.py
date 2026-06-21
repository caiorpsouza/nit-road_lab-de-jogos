from PPlay import *
from PPlay.sound import Music
import config
import sprites
import sounds
    

def play() :
    sounds.tocar_menu()
    botoes = [sprites.play_btn, sprites.diff_btn, sprites.scores_btn, sprites.quit_btn, sprites.volume_on, sprites.volume_off]
    while True:
        
        for botao in botoes:
            if config.janela.mouse.is_over_object(botao):
                botao.set_curr_frame(1)
            else:
                botao.set_curr_frame(0)


        #Clique no botão Sair
        if (config.janela.mouse.button_down(1) and config.janela.mouse.is_over_object(sprites.quit_btn)):
            config.is_running = False
            return 0
        if (config.janela.mouse.button_down(1) and config.janela.mouse.is_over_object(sprites.diff_btn)):
            config.Tela = 'Dificuldade'
            return 0
        if (config.janela.mouse.button_down(1) and config.janela.mouse.is_over_object(sprites.play_btn)):
            sounds.parar_menu()
            config.Tela = 'Fase_Selecao'
            return 0
        if (config.janela.mouse.button_down(1) and config.janela.mouse.is_over_object(sprites.scores_btn)):
            config.Tela = 'Ranking'
            return 0
        
        if (config.janela.mouse.button_down(1) and (config.janela.mouse.is_over_object(sprites.volume_on) or config.janela.mouse.is_over_object(sprites.volume_off))):
            config.volume = not config.volume
            sounds.aplicar_volume()
            
        sprites.background_menu.draw()
        sprites.title.draw()
        sprites.play_btn.draw()
        sprites.diff_btn.draw()
        sprites.scores_btn.draw()
        sprites.quit_btn.draw()

        if config.volume:
            sprites.volume_on.draw()
        else:
            sprites.volume_off.draw()



        config.janela.update()
