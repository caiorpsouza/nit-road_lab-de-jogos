from PPlay import sprite
import config
import sprites


def para_segundos(t):
    minutos, segundos = map(int, t.split(":"))
    return minutos * 60 + segundos


def draw_text_shadow(texto, x, y, tamanho, cor):
    config.janela.draw_text(
        texto, x + 2, y + 2,
        tamanho=tamanho,
        cor=(0, 0, 0),
        fonte="Arial"
    )

    config.janela.draw_text(
        texto, x, y,
        tamanho=tamanho,
        cor=cor,
        fonte="Arial"
    )


def cor_posicao(pos):
    if pos == 0:
        return (255, 215, 0)
    elif pos == 1:
        return (192, 192, 192)
    elif pos == 2:
        return (205, 127, 50)

    return (255, 255, 255)


def carregar_recordes():
    ranking = []

    with open("recordes.txt", "r") as arquivo:
        for linha in arquivo:
            nome, tempo, data = linha.strip().split(" - ")

            ranking.append({
                "nome": nome,
                "pontuacao": tempo,
                "data": data.split()[0]  # só a data
            })

    ranking.sort(key=lambda x: para_segundos(x["pontuacao"]))

    return ranking[:10]


def play():

    # Botando para carregar os recordes aqui pois dentro do while fica ineficiente.
    top10 = carregar_recordes()

    TABLE_WIDTH = 900

    inicio_x = (config.janela.largura - TABLE_WIDTH) / 2

    X_POS   = inicio_x
    X_NOME  = inicio_x + 100
    X_TEMPO = inicio_x + 420
    X_DATA  = inicio_x + 650

    titulo = "TOP 10 NITROAD"
    tam_titulo = 50

    # Aproximação da largura do texto (testei aqui e esse 0.8 deu bom)
    largura_titulo = len(titulo) * (tam_titulo * 0.8)

    x_titulo = config.janela.largura/2 - largura_titulo / 2

    while True:

        sprites.background_recordes.draw()


        draw_text_shadow(
            titulo,
            x_titulo,
            30,  # mais próximo do topo
            tam_titulo,
            (255, 255, 0)
        )

        draw_text_shadow("#", X_POS, 120, 35, (255, 255, 255))
        draw_text_shadow("NOME", X_NOME, 120, 35, (255, 255, 255))
        draw_text_shadow("TEMPO", X_TEMPO, 120, 35, (255, 255, 255))
        draw_text_shadow("DATA", X_DATA, 120, 35, (255, 255, 255))

        for i, item in enumerate(top10):

            y = 180 + i * 55

            cor = cor_posicao(i)

            draw_text_shadow(str(i + 1), X_POS, y, 35, cor)
            draw_text_shadow(item["nome"], X_NOME, y, 35, cor)
            draw_text_shadow(item["pontuacao"], X_TEMPO, y, 35, cor)
            draw_text_shadow(item["data"], X_DATA, y, 35, cor)

        draw_text_shadow(
            "ESC - VOLTAR",
            20,
            config.janela.altura - 50,
            25,
            (255, 255, 255)
        )

        if config.janela.keyboard.key_down("ESC"):
            config.Tela = "Menu"
            return

        config.janela.update()