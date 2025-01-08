# ------------ class setup ------------
class Location:
    def __init__(self,
                 name: str,
                 description: str,
                 lore: str,
                 ) -> None:
        self.name = name
        self.description = description
        self.lore = lore
        self.lore_unlocked = False
        self.visits = 0

    def look_around(self) -> str:
        you_see: str = f"{self.name} \n {self.description}"
        lore_skill_check = True
        if lore_skill_check :
            you_see += f"\n \n Ancient Lore : {self.lore}"
        return you_see

# ------------ object creation ------------
new_fort_cluckhaven = Location(name="New Fort Cluckhaven",
                               description='''  An impressive bastion of saftey for all of the Chickens,
 Ducks and Geese of Apple Tree Yard. It has solid walls, anti-weasel infiltration screens,
 sunbeam pass-through projectors, and has two seperate sets of feed and water spots.
    Best of all, it has ample extra space for everyone to roost. 
    Except for Cragglesnorts The Goose, of course, who refuses to climb up onto anything.''',
                               lore=''' Built by Mister Egg-Taker upon the ruins of the original Fort Cluckhaven,
 after Junior Egg-Taker destroyed the original early two Spring Times ago.'''
                               )

apple_tree_yard = Location(name="Apple Tree Yard",
                           description="A shaded, wonderful place that surrounds {new_fort_cluckhaven.name}. It has soft earth full of worms, apple trees taller than Missus Caresforus, branches only a Power Hop high to enjoy breezes in, and plenty of room for Duck Dashes and Goose Parades.",
                           lore="")

primrose_path = Location(name="the Primrose Path",
                    description="White gravel stones bordered by creeping thyme and fresh mint meanders along past a bird fountain. The path is further bordered by a solid wall of juniper and larch, kept neatly trimmed by Mister Egg Taker.",
                    lore="Sly The Fox is known to patrol this area, particularly around early evening. Missy Betty Buffsie insists he can be parlayed with."
                    )
