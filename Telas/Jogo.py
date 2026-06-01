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

        for veiculo in veiculos:
            player.check_atropelamento(veiculo)
        
        player.caiu_morreu(buracos)
        player.handle_input()

        player.move(tempo)

        if player.player_y + player.current_sprite.height <= 0:
            if config.fase < 2:
                config.fase += 1
                buracos, veiculos = carregar_fase(config.fase)
                player.volta_pro_inicio()
            else:
                player.volta_pro_inicio()

        player.update()
        player.draw()




