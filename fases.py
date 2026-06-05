import sprites

# A lane é dividida em 16 partes, o 1 é o topo da tela e o 16 é a parte mais baixa, onde o player começa.
phases = [
    {
        "background": sprites.fase1,
        "PropSpawners": [],
        "CarSpawners": [
            # Essas lanes sao das bicicletas
            {"lane": 3, "side": "right", "vehicles": ["ciclista-sexy"], "velocity": 100},
            {"lane": 4, "side": "right", "vehicles": ["vendedor_de_cana"], "velocity": 100},
            {"lane": 5, "side": "left", "vehicles": ["red_car", "yellow_car"], "velocity": 300},
            {"lane": 6, "side": "left", "vehicles": ["red_car"], "velocity": 250},
            {"lane": 7, "side": "right", "vehicles": ["yellow_car", "police_car"], "velocity": 300},
            {"lane": 8, "side": "right", "vehicles": ["police_car"], "velocity": 350},
            {"lane": 11, "side": "left", "vehicles": ["red_car"], "velocity": 400},
            {"lane": 12, "side": "left", "vehicles": ["yellow_car"], "velocity": 200},
            {"lane": 13, "side": "right", "vehicles": ["red_car", "yellow_car", "yellow_car"], "velocity": 200},
            {"lane": 14, "side": "right", "vehicles": ["red_car", "yellow_car", "yellow_car"], "velocity": 200}
        ],
        "buracos": 3,
        "terrains": {
            0: 'ground',
            1: 'ground',2: 'ground',3: 'ground',4: 'ground',
            5: 'ground',6: 'ground',7: 'ground',8: 'ground',
            9: 'ground',10: 'ground',11: 'ground',12: 'ground',
            13: 'ground',14: 'ground',15: 'ground',16: 'ground',
        }
    },
    {
        "background": sprites.fase2,
        "PropSpawners": [],
        "CarSpawners": [
            {"lane": 4, "side": "left", "vehicles": ["red_car", "yellow_car"], "velocity": 150},
            {"lane": 5, "side": "left", "vehicles": ["red_car", "police_car"], "velocity": 150},
            {"lane": 6, "side": "right", "vehicles": ["yellow_car"], "velocity": 150},
            {"lane": 7, "side": "left", "vehicles": ["police_car", "red_car"], "velocity": 150},
            {"lane": 8, "side": "left", "vehicles": ["yellow_car"], "velocity": 150},
            {"lane": 9, "side": "right", "vehicles": ["red_car"], "velocity": 150},
            {"lane": 12, "side": "left", "vehicles": ["yellow_car"], "velocity": 150},
            {"lane": 13, "side": "left", "vehicles": ["police_car"], "velocity": 150},
            {"lane": 14, "side": "right", "vehicles": ["red_car"], "velocity": 150},
        ],
        "buracos": 4,
        "terrains": {
            0: 'ground',
            1: 'ground',2: 'ground',3: 'ground',4: 'ground',
            5: 'ground',6: 'ground',7: 'ground',8: 'ground',
            9: 'ground',10: 'ground',11: 'ground',12: 'ground',
            13: 'ground',14: 'ground',15: 'ground',16: 'ground',
        }
    },
    {   
        "background": sprites.fase3,
        "PropSpawners": [
            {"lane": 8, "side": "left", "props": ["tire", "bed1", "bed2"], "velocity": 100},
            {"lane": 9, "side": "right", "props": ["tire", "bed1", "bed2"], "velocity": 100},
        ],
        "CarSpawners": [
            {"lane": 11, "side": "left", "vehicles": ["vendedor_de_cana", "vendedor_de_picole"], "velocity": 100},
            {"lane": 12, "side": "right", "vehicles": ["vendedor_de_cana", "vendedor_de_picole"], "velocity": 100},
        ],
        "buracos": 0,
        "terrains": {
            0: 'ground',
            1: 'ground',2: 'ground',3: 'ground',4: 'ground',
            5: 'ground',6: 'ground',7: 'ground',8: 'water',
            9: 'water',10: 'ground',11: 'ground',12: 'ground',
            13: 'ground',14: 'ground',15: 'ground',16: 'ground',
        }
    },
    
]


