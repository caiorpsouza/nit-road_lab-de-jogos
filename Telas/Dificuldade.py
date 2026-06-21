from PPlay import *
import config
import sprites
import sounds

opcao_selecionada = 0

opcoes_dificuldade = ["FACIL", "MEDIO", "DIFICIL"]

MENU_X = 220
MENU_Y_INICIAL = 220
MENU_SPACING = 70


def mouse_click():
    if config.janela.mouse.is_button_pressed(1):
        if not config.mouse_click_ativo:
            config.mouse_click_ativo = True
            return True
    else:
        config.mouse_click_ativo = False
    return False


def draw_text_shadow(texto, x, y, tamanho, cor):
    config.janela.draw_text(texto, x + 2, y + 2, tamanho=tamanho, cor=(0, 0, 0), fonte="Arial")
    config.janela.draw_text(texto, x, y, tamanho=tamanho, cor=cor, fonte="Arial")


def get_mouse_hover_index(mouse):
    mx, my = mouse.get_position()

    for i in range(4):
        y = MENU_Y_INICIAL + i * MENU_SPACING

        if MENU_X <= mx <= MENU_X + 600 and y <= my <= y + 40:
            return i

    return None


def aplicar_config(index, direction):

    if index == 0:
        config.dificuldade = max(1, min(3, config.dificuldade + direction))

    elif index == 1:
        config.definir_volume(config.volume + (0.05 * direction))
        sounds.aplicar_volume()

    elif index == 2:
        config.musica = not config.musica
        sounds.aplicar_volume()

    elif index == 3:
        config.efeitos = not config.efeitos
        sounds.aplicar_volume()


def play():
    global opcao_selecionada

    teclado = config.janela.keyboard
    mouse = config.janela.mouse

    while True:
        sprites.background_diff.draw()

        mx, my = mouse.get_position()
        hover = get_mouse_hover_index(mouse)
        
        if hover is not None:
            opcao_selecionada = hover

        clicou = mouse_click()

        if teclado.key_pressed("DOWN"):
            opcao_selecionada = (opcao_selecionada + 1) % 4

        if teclado.key_pressed("UP"):
            opcao_selecionada = (opcao_selecionada - 1) % 4

        if teclado.key_pressed("LEFT"):
            aplicar_config(opcao_selecionada, -1)

        if teclado.key_pressed("RIGHT"):
            aplicar_config(opcao_selecionada, 1)


        if clicou and hover is not None:
            
            if hover == 1: 
                # LÓGICA DO VOLUME
                barra_x = MENU_X + 200
                barra_w = 220
                
                if mx < barra_x + 20: 
                    aplicar_config(1, -1)
                elif mx > barra_x + barra_w - 20: 
                    aplicar_config(1, 1)

                else:
                    ratio = (mx - barra_x) / barra_w
                    ratio = max(0.0, min(1.0, ratio)) 
                    config.definir_volume(ratio)
                    sounds.aplicar_volume()
            
            else: 

                ponto_medio = MENU_X + 260 
                
                if mx < ponto_medio:
                    aplicar_config(hover, -1) # Clicou do lado esquerdo (<)
                else:
                    aplicar_config(hover, 1)  # Clicou do lado direito (>)

        draw_text_shadow("CONFIGURACOES", 350, 80, 40, (255, 255, 0))

        dificuldade_txt = opcoes_dificuldade[config.dificuldade - 1]

        volume_blocos = int(config.volume * 10)
        barra_volume = "█" * volume_blocos + "░" * (10 - volume_blocos)

        musica_txt = "ON" if config.musica else "OFF"
        efeitos_txt = "ON" if config.efeitos else "OFF"

        linhas = [
            f"DIFICULDADE   < {dificuldade_txt} >",
            f"VOLUME        < {barra_volume} >",
            f"MUSICA        < {musica_txt} >",
            f"EFEITOS       < {efeitos_txt} >"
        ]


        for i, texto in enumerate(linhas):
            y = MENU_Y_INICIAL + i * MENU_SPACING
            cor = (255, 255, 255)

            if i == opcao_selecionada:
                cor = (255, 255, 0)

            draw_text_shadow(texto, MENU_X, y, 28, cor)

        draw_text_shadow("ESC - VOLTAR", 20, config.janela.altura - 50, 22, (255, 255, 255))

        if teclado.key_down("ESC"):
            config.Tela = "Menu"
            return

        config.janela.update()