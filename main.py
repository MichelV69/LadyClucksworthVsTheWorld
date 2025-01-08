# ------------ imports ------------
import os
from character import Hero, Enemy
from weapon import short_bow, iron_sword
from language import *
from location import *

# ------------ setup ------------
hero = Hero(name="Hero", health=100, location=new_fort_cluckhaven)
hero.equip(iron_sword)
enemy = Enemy(name="Enemy", health=100, weapon=short_bow)

game_states: dict = {
    'menu': True,
    'movement' : False,
    'store1' : False,
    'scene1_finished': False
}

game_states['menu'] = False;
user_do: str = "init"

# ------------ game loop ------------
while user_do.lower() != 'q':
    os.system("clear")

    hero.surroundings()
    print("\n")
    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()

    user_do = input()
