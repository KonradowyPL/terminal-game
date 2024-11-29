from src.schedculer import schedcule
from src.enemy import Zomie, Spider, Creeper
import random

import src.schedculer as schedculer


weights = {
    Zomie: 1,
    Spider: 5,
    Creeper: 17,
}


def spawn(difficulty, world, player):
    delay = 0
    while difficulty > 0:
        delay += random.randint(7, 10)
        maxWeight = 0
        selectedEntity = Zomie
        for entity, weight in weights.items():
            if weight > maxWeight and weight <= difficulty:
                selectedEntity = entity
                maxWeight = weight
        enemy = selectedEntity(world.len*4-1, 3*4-1, -1, player)
        difficulty -= maxWeight
        schedculer.schedcule(delay, world.addEntity, enemy)


def spawner(difficulty, world, player):
    spawn(difficulty, world, player)
    schedcule(random.randint(20, 30),
              spawner,  difficulty + 1, world, player)
