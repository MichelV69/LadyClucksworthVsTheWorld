# ------------ imports ------------
from language import *
from weapon import fists
from health_bar import HealthBar
from location import *

# ------------ parent class setup ------------
class Bridge:
    def __init__(self, 
                 description: str, 
                 links_to: Location) -> None:
        self.description = description
        self.links_to = links_to

class Grid:
    def __init__(self,
                 current_location: Location,
                **connects_to: Bridge) -> None:
        self.current_location = current_location
        if connects_to["north"]:
            self.north = connects_to["north"]
        if connects_to["east"]:
            self.east = connects_to["east"]
        if connects_to["south"]:
            self.south = connects_to["south"]
        if connects_to["west"]:
            self.west = connects_to["west"]


class Map:
    def __init__(self,
                 name: str,
                 reference: list) -> None:
        self.name = name
        self.reference = reference
#----- end of file ----- 