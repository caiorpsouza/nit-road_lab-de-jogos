from PPlay import *
import config

play_btn = sprite.Sprite("images/play-button.png")
diff_btn = sprite.Sprite("images/diff-button.png")
scores_btn = sprite.Sprite("images/scores-button.png")
quit_btn = sprite.Sprite("images/quit-button.png")
background = sprite.Sprite("images/main-menu-background.jpeg")
title = sprite.Sprite("images/title.png")

background.set_position(0, 0)
title.set_position(config.janela.largura/2-title.width/2, 75)

play_btn.set_position(config.janela.largura/2-play_btn.width/2, title.y + title.height + 75)
diff_btn.set_position(config.janela.largura/2-diff_btn.width/2, play_btn.y + play_btn.height + 50)
scores_btn.set_position(config.janela.largura/2-scores_btn.width/2, diff_btn.y + diff_btn.height + 50)
quit_btn.set_position(config.janela.largura/2-quit_btn.width/2, scores_btn.y + scores_btn.height + 50)


def play() :
    while True:

        #Clique no botão Sair
        if (config.janela.mouse.button_down(1) and config.janela.mouse.is_over_object(quit_btn)):
            config.is_running = False
            return 0
        if (config.janela.mouse.button_down(1) and config.janela.mouse.is_over_object(diff_btn)):
            config.Tela = 'Dificuldade'
            return 0

        background.draw()
        title.draw()
        play_btn.draw()
        diff_btn.draw()
        scores_btn.draw()
        quit_btn.draw()

        config.janela.update()
