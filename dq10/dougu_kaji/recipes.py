import random

tyo_kagayakijueki = {
    'A': [155, 161],
    'B': [220, 230],
    'C': [155, 161],
    'D': [220, 230],
    'E': [140, 150],
    'F': [140, 150],
}

rnd = [random.randint(100, 230) for i in range(1, 7)]
tyo_random = {
    'A': 100,
    'B': [rnd[1], rnd[0] + random.randint(5, 10)],
    'C': 100,
    'D': [rnd[3], rnd[0] + random.randint(5, 10)],
    'E': 100,
    'F': [rnd[5], rnd[0] + random.randint(5, 10)],
}
