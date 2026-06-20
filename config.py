from PPlay import *
import pygame  # type: ignore[import-not-found]
from assets import resource_path

pygame.init()
janela = window.Window(1400, 960, "Nit Road")

info_tela = pygame.display.Info()
janela.real_screen = pygame.display.set_mode(
	(info_tela.current_w, info_tela.current_h),
	pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE,
)

keyboard = janela.keyboard
mouse = janela.mouse

icone = pygame.image.load(resource_path("images/logo/logo.png"))
pygame.display.set_icon(icone)


Tela = 'Menu'
dificuldade = 1
is_running = True

max_vidas = 5

volume = True

fase = 1


    