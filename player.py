from resources import Resource

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.resources = {Resource.BRICK: 0, Resource.WOOD: 0, Resource.WHEAT: 0, Resource.SHEEP: 0, Resource.ORE: 0}
        self.settlements = []
        self.cities = []
        self.roads = []
        self.victory_points = 0
        self.development_cards = []