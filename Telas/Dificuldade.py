from PPlay import *
import config
import sprites

def play() :
    botoes = [sprites.facil_btn, sprites.medio_btn, sprites.dificil_btn]
    while True:

        for botao in botoes:
            if config.janela.mouse.is_over_object(botao):
                botao.set_curr_frame(1)
            else:
                botao.set_curr_frame(0)

        #Clique nos botões
        if (config.janela.mouse.button_down(1) and config.janela.mouse.is_over_object(sprites.facil_btn)):
            config.dificuldade = 1

        if (config.janela.mouse.button_down(1) and config.janela.mouse.is_over_object(sprites.medio_btn)):
            config.dificuldade = 2

        if (config.janela.mouse.button_down(1) and config.janela.mouse.is_over_object(sprites.dificil_btn)):
            config.dificuldade = 3


        if (config.janela.keyboard.key_down('ESC')):
            config.Tela = 'Menu'
            return 0

        sprites.background_diff.draw()
        sprites.facil_btn.draw()
        sprites.medio_btn.draw()
        sprites.dificil_btn.draw()
        config.janela.update()
