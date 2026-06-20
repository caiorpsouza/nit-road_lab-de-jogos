import config
from PPlay import *
from assets import resource_path

# TITLE
title = sprite.Sprite(resource_path("images/title/title.png"))
title.set_position(config.janela.largura/2-title.width/2, 50)

# LIFES
life = sprite.Sprite(resource_path("images/vidas/pacoca_full.png"))

# BOTÕES
espaco =  100
y_inicial = config.janela.altura/2 - (3 * espaco)/2

facil_btn = sprite.Sprite(resource_path("images/buttons/easy-diff-button.png"), 2)
facil_btn.set_position(config.janela.largura/2-facil_btn.width/2, y_inicial)
medio_btn = sprite.Sprite(resource_path("images/buttons/medium-diff-button.png"), 2)
medio_btn.set_position(config.janela.largura/2-medio_btn.width/2, y_inicial + espaco)
dificil_btn = sprite.Sprite(resource_path("images/buttons/hard-diff-button.png"), 2)
dificil_btn.set_position(config.janela.largura/2-dificil_btn.width/2, y_inicial + 2 * espaco)

espaco = 120 
y_inicial = config.janela.altura/2 - (3 * espaco)/2

play_btn = sprite.Sprite(resource_path("images/buttons/play-button copy.png"), 2)
play_btn.set_position(config.janela.largura/2-play_btn.width/2, y_inicial)
diff_btn = sprite.Sprite(resource_path("images/buttons/diff-button copy.png"), 2)
diff_btn.set_position(config.janela.largura/2-diff_btn.width/2, y_inicial + espaco)
scores_btn = sprite.Sprite(resource_path("images/buttons/scores-button copy.png"), 2)
scores_btn.set_position(config.janela.largura/2-scores_btn.width/2, y_inicial + 2 * espaco)
quit_btn = sprite.Sprite(resource_path("images/buttons/quit-button copy.png"), 2)
quit_btn.set_position(config.janela.largura/2-quit_btn.width/2, y_inicial + 3 * espaco)


# BACKGROUND
background_menu = sprite.Sprite(resource_path("images/backgrounds/background-tarde.png"))
background_menu.set_position(0,0)
background_diff = sprite.Sprite(resource_path("images/backgrounds/background-dia.png"))
background_diff.set_position(0, 0)
fase1 = sprite.Sprite(resource_path("images/backgrounds/fase1.png"))
fase1.set_position(0, 0)
fase2 = sprite.Sprite(resource_path("images/backgrounds/fase2.png"))
fase2.set_position(0, 0)
fase3= sprite.Sprite(resource_path("images/backgrounds/fase3.png"))
fase3.set_position(0, 0)
fase4 = sprite.Sprite(resource_path("images/backgrounds/fase4.png"))
fase4.set_position(0, 0)


# PLAYER
player_up = sprite.Sprite(resource_path("images/player/player-up.png"), 4)
player_right = sprite.Sprite(resource_path("images/player/player-right.png"), 4)
player_left = sprite.Sprite(resource_path("images/player/player-left.png"), 4)
player_down = sprite.Sprite(resource_path("images/player/player-down.png"), 4)
player_crushing = sprite.Sprite(resource_path("images/player/player-crushing.png"), 4)
player_falling = sprite.Sprite(resource_path("images/player/player-falling.png"), 5)

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

# VOLUME 
volume_on = sprite.Sprite(resource_path("images/icon-sound/sound-on.png"), 2)
volume_on.set_position(config.janela.largura - volume_on.width - 10, 10)
volume_on.set_total_duration(200)
volume_on.set_loop(False)
volume_on.pause()
volume_off = sprite.Sprite(resource_path("images/icon-sound/sound-off.png"), 2)
volume_off.set_position(config.janela.largura - volume_off.width - 10, 10)
volume_off.set_total_duration(200)
volume_off.set_loop(False)  
volume_off.pause()

#VENDEDORES
vendedor_de_cana = sprite.Sprite(resource_path("images/vehicles/vendedor_de_cana_left.png"), 2)
vendedor_de_picole = sprite.Sprite(resource_path("images/vehicles/vendedor_de_picole_left.png"), 2)

#CICLISTAS
ciclista_sexy_right = sprite.Sprite(resource_path('images/vehicles/ciclista-sexy_right.png'),2)
ciclista_sexy_left = sprite.Sprite(resource_path('images/vehicles/ciclista-sexy_left.png'),2)

#CARROS
yellow_car = sprite.Sprite(resource_path('images/vehicles/yellow_car_left.png'), 2)
police_car = sprite.Sprite(resource_path('images/vehicles/police_car_left.png'), 2)
red_car = sprite.Sprite(resource_path('images/vehicles/red_car_left.png'), 2)
bus = sprite.Sprite(resource_path('images/vehicles/bus_left.png'), 2)
blue_car = sprite.Sprite(resource_path('images/vehicles/blue_car_left.png'), 2)

#MOTO
moto = sprite.Sprite(resource_path('images/vehicles/moto_left.png'), 2)

#SCOOTER
scooter = sprite.Sprite(resource_path('images/vehicles/scooter_left.png'), 2)

#CAMINHAO
caminhao = sprite.Sprite(resource_path('images/vehicles/caminhao_left.png'), 2)

#WATER PROPS
tire = sprite.Sprite(resource_path('images/props/tire.png'),2)
bed1 = sprite.Sprite(resource_path('images/props/bed1.png'),2)
bed2 = sprite.Sprite(resource_path('images/props/bed2.png'),2)



VEHICLES = {
    'yellow_car': yellow_car,
    'police_car': police_car,
    'red_car': red_car,
    'ciclista-sexy': ciclista_sexy_right,
    'vendedor_de_cana': vendedor_de_cana,
    'vendedor_de_picole': vendedor_de_picole,
    'bus': bus,
    'blue_car': blue_car,
    'moto': moto,
    'scooter': scooter,
    'caminhao': caminhao
}

PROPS = {
    'tire': tire,
    'bed1': bed1,
    'bed2': bed2,
}

#BURACO

buraco = sprite.Sprite(resource_path('images/obstacles/buraco.png'))