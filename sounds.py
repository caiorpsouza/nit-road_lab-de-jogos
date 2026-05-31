from PPlay import sound
import config

sons = {
    "jump": sound.Sound("sounds/jump-sound.ogg"),
    "menu_sound": sound.Sound("sounds/bossa-sound.ogg"),
}

menu_tocando = False

# mutar ou desmutar sons
def aplicar_volume():
    volume = 50 if config.volume else 0

    for som in sons.values():
        som.set_volume(volume)


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