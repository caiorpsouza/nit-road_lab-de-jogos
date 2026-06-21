import config
from Telas import Menu, Dificuldade, Fase_Selecao, Jogo, Ranking, Vitoria


while config.is_running:
    if config.Tela == 'Menu':
        Menu.play()
    elif config.Tela == 'Dificuldade':
        Dificuldade.play()
    elif config.Tela == 'Fase_Selecao':
        Fase_Selecao.play()
    elif config.Tela == 'Jogo':
        Jogo.jogo()
    elif config.Tela == 'Vitoria':
        Vitoria.play()
    elif config.Tela == 'Ranking':
        Ranking.play()