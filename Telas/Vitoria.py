import pygame
from assets import resource_path
from PPlay import *
import config
import sounds
import sprites
from datetime import datetime

def play():
    # Textos da tela de vitória
    titulo = sprite.Sprite(resource_path("images/title/voce_ganhou.png"))
    titulo.set_position(config.janela.largura/2 - titulo.width/2, 150)
    sounds.parar_game()
    if config.musica:
        sounds.winning_music.play()
    
    tempo_formatado = config.formatar_tempo(config.tempos_fases['total'])
    nome = ""
    
    while True:
        # Input do nome
        for evento in config.janela.eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    nome = nome[:-1]
                elif evento.unicode and evento.unicode.isprintable() and evento.unicode != ' ' and len(nome) < 12:
                    nome += evento.unicode

        if config.janela.keyboard.key_down('ENTER'):
            salvar_recorde(nome, config.tempos_fases['total'])
            config.Tela = 'Menu'
            sounds.winning_music.stop()
            return 0
        if config.janela.keyboard.key_down('ESC'):
            config.Tela = 'Menu'
            sounds.winning_music.stop()
            return 0
            
        # Desenhar
        sprites.background_menu.draw()
        titulo.draw()
        config.janela.draw_text(f"Tempo: {tempo_formatado}", config.janela.largura * 2/5, titulo.x + titulo.height + 100, tamanho=40, cor=(0,0,0), fonte="Arial")
        # Desenhar o nome que está sendo digitado
        config.janela.draw_text(nome + ("_" if int(pygame.time.get_ticks() / 500) % 2 == 0 else ""), config.janela.largura / 2 - 100, config.janela.altura / 3 + 350, tamanho=60, cor=(255, 255, 0), fonte="lucidaconsole")
        
        config.janela.update()

def salvar_recorde(nome, tempo_segundos):
    """Salva o recorde no arquivo recordes.txt"""
    tempo_formatado = config.formatar_tempo(tempo_segundos)
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    with open("recordes.txt", "a", encoding="utf-8") as f:
        f.write(f"{nome} - {tempo_formatado} - {timestamp}\n")
