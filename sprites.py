import config
from PPlay import *

# TITLE
title = sprite.Sprite("images/title/title.png")
title.set_position(config.janela.largura/2-title.width/2, 50)

# BOTÕES
espaco =  100
y_inicial = config.janela.altura/2 - (3 * espaco)/2

facil_btn = sprite.Sprite("images/buttons/easy-diff-button.png")
facil_btn.set_position(config.janela.largura/2-facil_btn.width/2, y_inicial)
medio_btn = sprite.Sprite("images/buttons/medium-diff-button.png")
medio_btn.set_position(config.janela.largura/2-medio_btn.width/2, y_inicial + espaco)
dificil_btn = sprite.Sprite("images/buttons/hard-diff-button.png")
dificil_btn.set_position(config.janela.largura/2-dificil_btn.width/2, y_inicial + 2 * espaco)

espaco = 120 
y_inicial = config.janela.altura/2 - (3 * espaco)/2

play_btn = sprite.Sprite("images/buttons/play-button copy.png")
play_btn.set_position(config.janela.largura/2-play_btn.width/2, y_inicial)
diff_btn = sprite.Sprite("images/buttons/diff-button copy.png")
diff_btn.set_position(config.janela.largura/2-diff_btn.width/2, y_inicial + espaco)
scores_btn = sprite.Sprite("images/buttons/scores-button copy.png")
scores_btn.set_position(config.janela.largura/2-scores_btn.width/2, y_inicial + 2 * espaco)
quit_btn = sprite.Sprite("images/buttons/quit-button copy.png")
quit_btn.set_position(config.janela.largura/2-quit_btn.width/2, y_inicial + 3 * espaco)


# BACKGROUND
background_menu = sprite.Sprite("images/backgrounds/background-tarde.png")
background_menu.set_position(0,0)
background_diff = sprite.Sprite("images/backgrounds/background-dia.png")
background_diff.set_position(0, 0)
fase1 = sprite.Sprite("images/backgrounds/fase1.png")
fase1.set_position(0, 0)
fase2 = sprite.Sprite("images/backgrounds/fase2.png")
fase2.set_position(0, 0)


# PLAYER
player_up = sprite.Sprite("images/player/player-up.png", 4)
player_right = sprite.Sprite("images/player/player-right.png", 4)
player_left = sprite.Sprite("images/player/player-left.png", 4)
player_down = sprite.Sprite("images/player/player-down.png", 4)
player_crushing = sprite.Sprite("images/player/jogador-crushing.png", 4)
player_falling = sprite.Sprite("images/player/jogador-falling.png", 4)

player_up.set_total_duration(333)
player_right.set_total_duration(333)
player_left.set_total_duration(333)
player_down.set_total_duration(333)

player_crushing.set_total_duration(800)
player_falling.set_total_duration(800)

# Desabilitar loop para animação tocar apenas uma vez
player_up.set_loop(False)
player_right.set_loop(False)
player_left.set_loop(False)
player_down.set_loop(False)
player_crushing.set_loop(False)
player_falling.set_loop(False)

player_up.pause()
player_right.pause()
player_left.pause()
player_down.pause()

# Volume icon
# VOLUME 
volume_on = sprite.Sprite("images/icon-sound/sound-on.png", 1)
volume_on.set_position(config.janela.largura - volume_on.width - 10, 10)
volume_off = sprite.Sprite("images/icon-sound/sound-off.png", 1)
volume_off.set_position(config.janela.largura - volume_off.width - 10, 10)

#CARROS


yellow_car = sprite.Sprite('images/vehicles/yellow_car_left_new.png', 2)
yellow_car.set_total_duration(500)
police_car = sprite.Sprite('images/vehicles/police_car_left_new.png', 2)
police_car.set_total_duration(500)
red_car = sprite.Sprite('images/vehicles/red_car_left_new.png', 2)
red_car.set_total_duration(500)
VEHICLES = {
    'yellow_car': yellow_car,
    'police_car': police_car,
    'red_car': red_car
}

#BURACO

buraco = sprite.Sprite('images/obstacles/buraco.png')