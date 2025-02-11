# ------------ imports ------------
import os
from character import Hero, Enemy
from weapon import short_bow, iron_sword
from language import *
from location import *
from map import *
from ansi_out import * 

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
list_of_scene_settings = []
### scene 1 : new_fort_cluckhaven
link_north = LinkDetails("apple_tree_yard", "hole in the fence",
                    apple_tree_yard)

scene_setting = TravelLink(new_fort_cluckhaven,
                     Direction.NORTH, link_north )

list_of_scene_settings.append(scene_setting)

### scene 2 : apple_tree_yard
link_west = LinkDetails("primrose_path", "opened garden gate",
                   primrose_path)

scene_setting = TravelLink(apple_tree_yard,
                     Direction.WEST, link_west )

list_of_scene_settings.append(scene_setting)

### scene 3 : primrose_path


### assemble map
game_world = Map("World_of_Lady_Clucksworth",
                 list_of_scene_settings)

## --- prime game loop menu
game_states['menu'] = False;
user_do: str = "init"

# ------------ game loop ------------
while user_do.lower() != 'q':
    os.system("clear")

    available_player_options: list = []
    can_travel = False;
    hero.surroundings()
    for travel_direction in game_world.get_available_destinations(hero.location):
        print(f"  * {travel_direction}\n")
        can_travel = True;
    print("\n")

    if can_travel:
        available_player_options.append("Go <direction>")

    available_player_options.append("q (to quit)")

    option_text: str = "\n ... you can: "
    for option in available_player_options:
        option_text += f"{option}, "

    option_text = option_text.rstrip()
    if option_text[-1] == ",":
        option_text = option_text.rstrip(",") + "."

    print(option_text) 

##/*
##    hero.attack(enemy)
##    enemy.attack(hero)
##
##    hero.health_bar.draw()
##    enemy.health_bar.draw()
##*/
    user_do = input(ANSI.colors["blue"]+" choice >> " + ANSI.colors["purple"])

    print(ANSI.colors["default"]+"\n")
# ------ end of file -----
