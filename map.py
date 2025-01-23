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
        if "north" in connects_to:
            self.north = connects_to["north"]
        if "east" in connects_to:
            self.east = connects_to["east"]
        if "south" in connects_to:
            self.south = connects_to["south"]
        if "west" in connects_to:
            self.west = connects_to["west"]

class Map:
    def __init__(self,
                 name: str,
                 scene_settings: list) -> None:
        self.name = name
        self.scene_settings = scene_settings

    def get_available_destinations(self, hero_location: Location) -> None:
        if hero_location.name in self.get_all_location_names():
            print(f"Found {hero_location.name}")

    def get_all_location_names(self) -> list:
        result: list = []
        for location_name in self.scene_settings.name:
            result.append(location_name)
        return result
#----- end of file -----
