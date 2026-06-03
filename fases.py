import sprites

# A lane é dividida em 16 partes, o 1 é o topo da tela e o 16 é a parte mais baixa, onde o player começa.

phases = [
    {
        "background": sprites.fase1,
        "spawners": [
            # Essas lanes sao das bicicletas
            # {"lane": 3, "side": "left", "vehicles": ["red_car", "yellow_car", "yellow_car"], "velocity": 150},
            # {"lane": 4, "side": "left", "vehicles": ["red_car"], "velocity": 150},
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
    },
    {
        "background": sprites.fase2,
        "spawners": [
            {"lane": 4, "side": "left", "vehicles": ["red_car", "yellow_car"], "velocity": 150},
            {"lane": 5, "side": "left", "vehicles": ["red_car", "police_car"], "velocity": 150},
            {"lane": 6, "side": "right", "vehicles": ["yellow_car"], "velocity": 150},
            {"lane": 7, "side": "right", "vehicles": ["police_car", "red_car"], "velocity": 150},
            {"lane": 8, "side": "right", "vehicles": ["yellow_car"], "velocity": 150},
            {"lane": 9, "side": "right", "vehicles": ["red_car"], "velocity": 150},
            {"lane": 12, "side": "left", "vehicles": ["yellow_car"], "velocity": 150},
            {"lane": 13, "side": "left", "vehicles": ["police_car"], "velocity": 150},
            {"lane": 14, "side": "right", "vehicles": ["red_car"], "velocity": 150},
        ],
        "buracos": 4,
    },
    {
        "spawners": [
            {"lane": 6, "side": "left", "vehicles": ["red_car", "yellow_car", "police_car"]},
            {"lane": 9, "side": "left", "vehicles": ["red_car"]},
            {"lane": 12, "side": "right", "vehicles": ["yellow_car", "police_car"]},
        ],
        "buracos": 5,
    },
]


