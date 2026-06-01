import fases
import sounds
import config
import sprites
from entities import Player, CarSpawner, Buraco


def carregar_fase(numero_fase):
    fase = fases.phases[numero_fase - 1]
    buracos = Buraco.buraco_generator(fase["buracos"])
    veiculos = []

    for spawner_info in fase["spawners"]:
        veiculo_spawner = CarSpawner.CarSpawner(
            spawner_info["lane"],
            spawner_info["side"],
            spawner_info["vehicles"],
            spawner_info["velocity"],
        )
        veiculos.append(veiculo_spawner)

    return buracos, veiculos

def jogo():
   
    sounds.tocar_game()
    config.fase = 1
    player = Player.Player("Player1", 3, 100)
    buracos, veiculos = carregar_fase(config.fase)


    tempo = 0
    while True:

        config.janela.clear()
        fases.phases[config.fase - 1]["background"].draw()

        dt = config.janela.delta_time()
        tempo += dt

        if config.keyboard.key_pressed("ESC"):
            sounds.parar_game()
            config.Tela = "Menu"
            return
        
        Buraco.buraco_drawer(buracos)

        for veiculo in veiculos:
            veiculo.loop()
        
        player.caiu_morreu(buracos)

        player.move(tempo)

        # Verificar se o player chegou ao topo da tela para avançar de fase
        if player.player_y + player.current_sprite.height <= 0:
            if config.fase < 2:
                config.fase += 1
                buracos, veiculos = carregar_fase(config.fase)
                player.volta_pro_inicio()
            else:
                player.volta_pro_inicio()

        carros_atras = []
        carros_na_frente = []
        carros_normais = []

        centro_player = player.player_y + player.current_sprite.height / 2

          
        for veiculo in veiculos:
            if veiculo.lane == player.get_lane():
                player.check_atropelamento(veiculo)

            # Isso daqui é para mudar a sobreposicao de player e carro, para o player ficar atrás do carro se ele estiver atrás e na frente se ele estiver na frente.
            if veiculo.lane == player.get_lane() - 1 or veiculo.lane == player.get_lane() + 1:
                for carro in veiculo.carros:
                    centro_carro = carro.sprite.y + carro.sprite.height / 2

                    if centro_player < centro_carro:
                        carros_na_frente.append(carro)
                    else:
                        carros_atras.append(carro)
            else:
                carros_normais.extend(veiculo.carros)

        player.update()

        # Carros que nao estao na mesma lane do player
        for carro in carros_normais:
            carro.draw()

        # Carro atras do player
        for carro in carros_atras:
            carro.draw()

        player.draw()

        # Carro na frente do player
        for carro in carros_na_frente:
            carro.draw()




