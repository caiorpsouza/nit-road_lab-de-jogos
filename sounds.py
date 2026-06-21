from PPlay import sound
import config
from assets import resource_path

death_music = sound.Music(resource_path("sounds/Before_the_Final_Breath.ogg"))
winning_music = sound.Music(resource_path("sounds/Ascension_of_Crowns.ogg"))
sons = {
    "jump": sound.Sound(resource_path("sounds/jump-sound.ogg")),
    "menu_sound": sound.Sound(resource_path("sounds/bossa-sound.ogg")),
    "game_sound": sound.Sound(resource_path("sounds/The_Rush_at_Avenida.ogg"))
}

menu_tocando = False
game_tocando = False

# mutar ou desmutar sons
def aplicar_volume():
    volume = 50 if config.volume else 0

    for som in sons.values():
        som.set_volume(volume)

def tocar_game():
    global game_tocando

    if not game_tocando:
        sons["game_sound"].play(-1)
        game_tocando = True

def parar_game():   
    global game_tocando

    sons["game_sound"].stop()
    game_tocando = False

def tocar_menu():
    global menu_tocando

    if not menu_tocando:
        sons["menu_sound"].play(-1)
        menu_tocando = True


def parar_menu():
    global menu_tocando

    sons["menu_sound"].stop()
    menu_tocando = False


aplicar_volume()