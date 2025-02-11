# ------------ imports ------------
from enum import Enum
from language import *
from weapon import fists
from health_bar import HealthBar
from location import *

# ------------  supporting enums  ------------
Direction = Enum('Direction', [('NORTH',0), ('EAST', 90), ('SOUTH', 180), ('WEST', 270)])

# ------------ parent class setup ------------
class LinkDetails:
    def __init__(self,
                 short_name: str,
                 description: str,
                 links_to: Location) -> None:
        self.short_name = short_name
        self.description = description
        self.links_to = links_to

class TravelLink:
    def __init__(self,
                 current_location: Location,
                 travel_direction: Direction,
                 connects_to: LinkDetails) -> None:
        self.current_location = current_location
        self.travel_direction = travel_direction
        if connects_to is not None:
            self.connects_to = connects_to

class Map:
    def __init__(self,
                 name: str,
                 travel_links: list) -> None:
        self.name = name
        self.travel_links = travel_links

    def get_available_destinations(self, hero_location: Location) -> None:
        if hero_location.name in self.get_all_location_names():
            print(f"Found {hero_location.name}")

    def get_all_location_names(self) -> list:
        result: list = []
        for link_details in self.travel_links:
            result.append(link_details.connects_to.short_name)
        return result
#----- end of file -----
