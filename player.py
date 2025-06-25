class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.resources = []
        self.settlements = []
        self.cities = []
        self.roads = []
        self.victory_points = 0
        self.development_cards = []