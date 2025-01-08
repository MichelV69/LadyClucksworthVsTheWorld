# ------------ imports ------------
import os
from character import Hero, Enemy
from weapon import short_bow, iron_sword

# ------------ setup ------------
hero = Hero(name="Hero", health=100)
hero.equip(iron_sword)
enemy = Enemy(name="Enemy", health=100, weapon=short_bow)

game_states: dict = {
    'menu': True,
    'movement' : False,
    'store1' : False,
    'scene1_finished': False
}

game_states.menu = False;

# ------------ game loop ------------
while True:
    os.system("cls")

    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()

    input()
