from Telas import Derrota
import fases
import sounds
import config
import sprites
from entities import LifeDisplay, Player, CarSpawner, Buraco, PropSpawner


def carregar_fase(numero_fase):
    fase = fases.phases[numero_fase - 1]
    buracos = Buraco.buraco_generator(fase["buracos"])
    veiculos = []
    props = []

    for spawner_info in fase["CarSpawners"]:
        veiculo_spawner = CarSpawner.CarSpawner(
            spawner_info["lane"],
            spawner_info["side"],
            spawner_info["vehicles"],
            spawner_info["velocity"],
        )
        veiculos.append(veiculo_spawner)

    for spawner_info in fase["PropSpawners"]:
        prop_spawner = PropSpawner.PropSpawner(
            spawner_info["lane"],
            spawner_info["side"],
            spawner_info["props"],
            spawner_info["velocity"],
        )
        props.append(prop_spawner)
    


    return buracos, veiculos, props

def jogo():
   
    sounds.tocar_game()
    life_display = LifeDisplay.LifeDisplay()
    player = Player.Player("Player1", config.max_vidas, 100)
    buracos, veiculos, props = carregar_fase(config.fase)


    tempo = 0
    tempo_da_fase = 0
    tempo_salvo = False
    while True:

        config.janela.clear()
        fases.phases[config.fase - 1]["background"].draw()

        dt = config.janela.delta_time()
        tempo += dt
        tempo_da_fase += dt
        if config.keyboard.key_pressed("ESC"):
            sounds.parar_game()
            config.Tela = "Menu"
            return
        
        life_display.loop()
        life_display.lifes = player.retorna_vidas()

        Buraco.buraco_drawer(buracos)

        for prop_spawner in props:
            prop_spawner.loop()

        for veiculo in veiculos:
            veiculo.loop()
        
        player.move(tempo)
        player.try_land_on_props(props)
        player.check_afogamento()
        player.update_on_props(props)
        player.caiu_morreu(buracos)

        if config.fase == 4 and player.get_lane()<= 5:
                # Jogador completou todas as fases!
                config.salvar_tempo_fase(config.fase, tempo_da_fase)
                sounds.parar_game()
                config.tempo_ultima_fase = tempo
                config.Tela = 'Vitoria'
                return 0
        if player.player_y + player.current_sprite.height / 2 <= 0:
            
            # Salvar o tempo da fase apenas uma vez
            config.salvar_tempo_fase(config.fase, tempo_da_fase)
            
            # Verificar se completou a última fase
            
            # Desbloqueia a próxima fase
            config.desbloquear_fase(config.fase + 1)
            config.fase += 1
            buracos, veiculos, props = carregar_fase(config.fase)
            tempo_da_fase = 0
            
            player.volta_pro_inicio()

        carros_atras = []
        carros_na_frente = []
        print(config.tempos_fases)
        centro_player = player.current_sprite.y + player.current_sprite.height / 2

          
        for veiculo in veiculos:
            if veiculo.lane == player.get_lane():
                player.check_atropelamento(veiculo)
            for carro in veiculo.carros:
                centro_carro = carro.sprite.y + carro.sprite.height / 2

                if centro_player < centro_carro:
                    carros_na_frente.append(carro)
                else:
                    carros_atras.append(carro)

        for prop in props:
            prop.draw()
            
        player.update()

        # Carro atras do player
        for carro in carros_atras:
            carro.draw()

        player.draw()

        for carro in carros_na_frente:
            carro.draw()
        
        if life_display.lifes == 0:
            
            Derrota.play()
            life_display.lifes = config.max_vidas
            return 0