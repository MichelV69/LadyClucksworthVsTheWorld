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
        self.description: description
        self.links_to: links_to

class Grid:
    def __init__(self,
                 current_location: Location,
                 north: Location,
                 east: Location,
                 south: Location,
                 west: Location,
                 special: Bridge) -> None:
        self.current_location = current_location
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.special = special

class Map:
    def __init__(self,
                 name: str,
                 reference: List(Grid)) -> None:
        self.name = name
        self.reference = reference
#----- end of file ----- 