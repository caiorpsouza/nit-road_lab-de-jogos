from PPlay import *
import config

facil_btn = sprite.Sprite("images/easy-diff-button.png")
medio_btn = sprite.Sprite("images/medium-diff-button.png")
dificil_btn = sprite.Sprite("images/hard-diff-button.png")
background = sprite.Sprite("images/diff-menu-background.jpg")
background.set_position(0,0)
medio_btn.set_position(config.janela.largura/2-medio_btn.width/2, config.janela.altura/2 - medio_btn.height/2)
facil_btn.set_position(config.janela.largura/2-facil_btn.width/2, medio_btn.y - facil_btn.height - 100)
dificil_btn.set_position(config.janela.largura/2-dificil_btn.width/2, medio_btn.y + dificil_btn.height + 100)
        


def play() :
    while True:


        #Clique nos botões
        if (config.janela.mouse.button_down(1) and config.janela.mouse.is_over_object(facil_btn)):
            config.dificuldade = 1

        if (config.janela.mouse.button_down(1) and config.janela.mouse.is_over_object(medio_btn)):
            config.dificuldade = 2

        if (config.janela.mouse.button_down(1) and config.janela.mouse.is_over_object(dificil_btn)):
            config.dificuldade = 3


        if (config.janela.keyboard.key_down('ESC')):
            config.Tela = 'Menu'
            return 0

        background.draw()
        facil_btn.draw()
        medio_btn.draw()
        dificil_btn.draw()
        config.janela.update()
        print(config.dificuldade)
