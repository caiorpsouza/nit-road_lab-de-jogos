from PPlay import *
import config
import sprites

def play():
    botoes = [sprites.fase1_btn, sprites.fase2_btn, sprites.fase3_btn, sprites.fase4_btn]
    while True:

        for i, botao in enumerate(botoes):
            numero_fase = i + 1
            # Se a fase está desbloqueada, permite interação
            if numero_fase in config.fases_desbloqueadas:
                if config.janela.mouse.is_over_object(botao):
                    botao.set_curr_frame(1)
                else:
                    botao.set_curr_frame(0)
            else:
                # Fase travada - deixa sempre no frame 0 (desativado)
                botao.set_curr_frame(0)

        # Clique nos botões
        if (config.janela.mouse.button_down(1) and config.janela.mouse.is_over_object(sprites.fase1_btn)):
            if 1 in config.fases_desbloqueadas:
                config.fase = 1
                config.Tela = 'Jogo'
                return 0

        if (config.janela.mouse.button_down(1) and config.janela.mouse.is_over_object(sprites.fase2_btn)):
            if 2 in config.fases_desbloqueadas:
                config.fase = 2
                config.Tela = 'Jogo'
                return 0

        if (config.janela.mouse.button_down(1) and config.janela.mouse.is_over_object(sprites.fase3_btn)):
            if 3 in config.fases_desbloqueadas:
                config.fase = 3
                config.Tela = 'Jogo'
                return 0

        if (config.janela.mouse.button_down(1) and config.janela.mouse.is_over_object(sprites.fase4_btn)):
            if 4 in config.fases_desbloqueadas:
                config.fase = 4
                config.Tela = 'Jogo'
                return 0

        if (config.janela.keyboard.key_down('ESC')):
            config.Tela = 'Menu'
            return 0

        sprites.background_fase_selecao.draw()
        sprites.fase1_btn.draw()
        sprites.fase2_btn.draw()
        sprites.fase3_btn.draw()
        sprites.fase4_btn.draw()
        
        # Desenhar cadeado nas fases travadas e tempos nas desbloqueadas
        for i, botao in enumerate(botoes):
            numero_fase = i + 1
            if numero_fase not in config.fases_desbloqueadas:
                # Centralizar o cadeado no botão
                lock_x = botao.x + botao.width / 2 - sprites.locked_icon.width / 2
                lock_y = botao.y + botao.height / 2 - sprites.locked_icon.height / 2
                sprites.locked_icon.set_position(lock_x, lock_y)
                sprites.locked_icon.draw()
            else:
                # Mostrar tempo da fase
                tempo_fase = config.obter_tempo_fase(numero_fase)
                if tempo_fase is not None:
                    tempo_formatado = config.formatar_tempo(tempo_fase)
                    config.janela.draw_text(tempo_formatado,botao.x + botao.width/3 + 15,botao.y+botao.height,tamanho=24,cor=(255,255,255), fonte="Arial")

        
        config.janela.update()
