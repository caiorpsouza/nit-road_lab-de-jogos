from PPlay import *
import pygame  # type: ignore[import-not-found]
from assets import resource_path
import json
import os

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

fase = 1

volume = 0.7
volume_anterior = volume

musica = True

efeitos = True

mouse_click_ativo = False


def multiplicador_dificuldade():
    return {
        1: 1,
        2: 1.2,
        3: 1.5,
    }.get(dificuldade, 1.0)


def multiplicador_spawn_dificuldade():
    return {
        1: 1.15,
        2: 1.0,
        3: 0.9,
    }.get(dificuldade, 1.0)


def definir_volume(novo_volume):
    global volume, volume_anterior
    volume = max(0.0, min(1.0, novo_volume))
    if volume > 0:
        volume_anterior = volume


def alternar_volume():
    global volume, volume_anterior
    if volume > 0:
        volume_anterior = volume
        volume = 0
    else:
        volume = volume_anterior if volume_anterior > 0 else 0.7

# Sistema de desbloqueio de fases e tempos
save_file = "save.json"

def carregar_progresso():
    global fases_desbloqueadas, tempos_fases
    if os.path.exists(save_file):
        with open(save_file, 'r') as f:
            dados = json.load(f)
            fases_desbloqueadas = set(dados.get("fases_desbloqueadas", [1]))
            tempos_fases = dados.get("tempos_fases", {})
    else:
        fases_desbloqueadas = {1}
        tempos_fases = {'total': 0}

def salvar_progresso():
    with open(save_file, 'w') as f:
        json.dump({
            "fases_desbloqueadas": list(fases_desbloqueadas),
            "tempos_fases": tempos_fases
        }, f)

def desbloquear_fase(numero_fase):
    global fases_desbloqueadas
    if numero_fase not in fases_desbloqueadas:
        fases_desbloqueadas.add(numero_fase)
        salvar_progresso()

def salvar_tempo_fase(numero_fase, tempo_segundos):
    global tempos_fases
    tempo_atual = tempos_fases.get(str(numero_fase), None)
    # Salvar apenas se for a primeira vez ou se for um novo recorde (menor tempo)
    if tempo_atual is None or tempo_segundos < tempo_atual:
        tempos_fases[str(numero_fase)] = tempo_segundos
        tempos_fases['total'] = 0
        for i in range(4):
        	if tempos_fases.get(str(i), None) != None:
                  tempos_fases['total'] += tempos_fases[str(i)]
				
        salvar_progresso()
        return True  # Novo recorde!
    return False  # Não é recorde

def obter_tempo_fase(numero_fase):
    return tempos_fases.get(str(numero_fase), None)

def formatar_tempo(segundos):
    """Converte segundos para formato MM:SS"""
    minutos = int(segundos) // 60
    segs = int(segundos) % 60
    return f"{minutos:02d}:{segs:02d}"

fases_desbloqueadas = {1}
tempos_fases = {'total': 0}
tempo_ultima_fase = 0  # Armazena o tempo da última fase completada
carregar_progresso()