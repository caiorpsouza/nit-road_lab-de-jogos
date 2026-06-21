from PPlay import sprite
import config

background = sprite.Sprite("images/backgrounds/background-tarde.png")
background.set_position(0, 0)

def para_segundos(t):
    minutos, segundos = map(int, t.split(":"))
    return minutos * 60 + segundos

def play() :
    while True:
        background.draw()

        with open('recordes.txt', 'r') as arquivo:
            saida = []
            for linha in arquivo:
                nome, tempo, data = linha.strip().split(" - ")
                saida.append({"nome": nome,"pontuacao": tempo,"data": data})

            saida.sort(key=lambda x: para_segundos(x["pontuacao"]))

            top10 = saida[:10]    
            i = 0
            for item in top10:
                config.janela.draw_text(f"{i+1}", config.janela.largura * 1/10, config.janela.altura/5 + i * 50, tamanho=35, cor=(10, 10, 255), fonte="Arial")
                config.janela.draw_text(f"{item['nome']}", config.janela.largura * 2/10 , config.janela.altura/5 + i * 50, tamanho=35, cor=(10, 10, 255), fonte="Arial")
                config.janela.draw_text(f"{item['pontuacao']}", config.janela.largura * 4/10, config.janela.altura/5 + i * 50, tamanho=35, cor=(10, 10, 255), fonte="Arial")
                config.janela.draw_text(f"{item['data']} ", config.janela.largura * 6/10, config.janela.altura/5 + i * 50, tamanho=35, cor=(10, 10, 255), fonte="Arial")
                i+=1

            config.janela.draw_text("#", config.janela.largura * 1/10, config.janela.altura/7 , tamanho=35, cor=(10, 10, 255), fonte="Arial")
            config.janela.draw_text("NOME", config.janela.largura * 2/10 , config.janela.altura/7 , tamanho=35, cor=(10, 10, 255), fonte="Arial")
            config.janela.draw_text("PONTOS", config.janela.largura * 4/10, config.janela.altura/7 , tamanho=35, cor=(10, 10, 255), fonte="Arial")
            config.janela.draw_text("DATA", config.janela.largura * 6/10, config.janela.altura/7 , tamanho=35, cor=(10, 10, 255), fonte="Arial")


        #Saída para o menu principal
        if (config.janela.keyboard.key_down('ESC')):
            config.Tela = 'Menu'
            return 0
        
        config.janela.update()
