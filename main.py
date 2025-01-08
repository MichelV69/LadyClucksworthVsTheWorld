# ------------ imports ------------
import os
from character import Hero, Enemy
from weapon import short_bow, iron_sword
from language import *
from location import *
from map import *

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

## --- build world map
list_of_grid_references = []
## scene 1 : new_fort_cluckhaven
link_north = Bridge("hole in the fence", 
                    apple_tree_yard)

scene_setting = Grid(new_fort_cluckhaven, 
                     north= link_north )

list_of_grid_references.append(scene_setting)

## scene 2 : apple_tree_yard

## scene 3 : primrose_path

game_world = Map("World_of_Lady_Clucksworth", 
                 list_of_grid_references)

## --- prime game loop menu
game_states['menu'] = False;
user_do: str = "init"

# ------------ game loop ------------
while user_do.lower() != 'q':
    os.system("clear")

    hero.surroundings()
    print("\n")
   
##/*
##    hero.attack(enemy)
##    enemy.attack(hero)
##
##    hero.health_bar.draw()
##    enemy.health_bar.draw()
##*/
    user_do = input(HealthBar.colors["blue"]+" > " + HealthBar.colors["purple"])
