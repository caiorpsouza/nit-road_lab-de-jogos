from PPlay import sound
import config
from assets import resource_path

death_music = sound.Sound(resource_path("sounds/Before_the_Final_Breath.ogg"))
winning_music = sound.Sound(resource_path("sounds/Ascension_of_Crowns.ogg"))
sons = {
    "jump": sound.Sound(resource_path("sounds/jump-sound.ogg")),
    "menu_sound": sound.Sound(resource_path("sounds/bossa-sound.ogg")),
    "game_sound": sound.Sound(resource_path("sounds/The_Rush_at_Avenida.ogg"))
}

menu_tocando = False
game_tocando = False

# mutar ou desmutar sons
def aplicar_volume():
    volume = int(max(0.0, min(1.0, config.volume)) * 100)

    for nome, som in sons.items():
        if nome == "jump":
            som.set_volume(volume if config.efeitos else 0)
        else:
            som.set_volume(volume if config.musica else 0)

    death_music.set_volume(volume if config.musica else 0)
    winning_music.set_volume(volume if config.musica else 0)

def tocar_game():
    global game_tocando

    if not game_tocando and config.musica:
        sons["game_sound"].play(-1)
        game_tocando = True

def parar_game():   
    global game_tocando

    sons["game_sound"].stop()
    game_tocando = False

def tocar_menu():
    global menu_tocando

    if not menu_tocando and config.musica:
        sons["menu_sound"].play(-1)
        menu_tocando = True


def parar_menu():
    global menu_tocando

    sons["menu_sound"].stop()
    menu_tocando = False


aplicar_volume()