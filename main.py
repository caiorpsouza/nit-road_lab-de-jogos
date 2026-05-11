import config
from Telas import Menu, Dificuldade


while config.is_running:
    if config.Tela == 'Menu':
        Menu.play()
    if config.Tela == 'Dificuldade':
        Dificuldade.play()