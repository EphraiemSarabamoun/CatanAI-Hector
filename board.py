import random
from resources import Resource
from hexes import Hex
from edges import Edge


class Board:
    def __init__(self):
        self.hexes = []
        self.edges = []


    def generate_board(self):
                # Resource distribution for a standard Catan game
        self.resource_pool = ([Resource.WOOD] * 4 +
                              [Resource.SHEEP] * 4 +
                              [Resource.WHEAT] * 4 +
                              [Resource.BRICK] * 3 +
                              [Resource.ORE] * 3 +
                              [Resource.NONE]) # The desert
        random.shuffle(self.resource_pool)

        # Number token distribution
        self.values_pool = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        random.shuffle(self.values_pool)

        resource = self.resource_pool.pop()
        value = 0
        if resource is not Resource.NONE:
            value = self.values_pool.pop()
        
        first_hex = Hex(resource, value)

        # Create 6 edges for the hex
        hex_edges = [Edge() for _ in range(6)]

        # Link edges to each other and to the hex's resource
        for i in range(6):
            current_edge = hex_edges[i]
            
            # Assign the hex's resource
            current_edge.resources.append(first_hex.resource)

            # Connect to adjacent edges in the cycle
            # The previous edge is at index (i - 1)
            # The next edge is at index (i + 1) % 6
            prev_edge = hex_edges[i - 1]
            next_edge = hex_edges[(i + 1) % 6]
            
            current_edge.connections.append(prev_edge)
            current_edge.connections.append(next_edge)

        # Add the new edges to the hex and the board
        first_hex.edges.extend(hex_edges)
        self.edges.extend(hex_edges)
            
        self.hexes.append(first_hex)




