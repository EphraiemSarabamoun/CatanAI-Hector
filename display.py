import pygame
import math
from board import Board
from resources import Resource

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
HEX_SIZE = 40

# --- Colors ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RESOURCE_COLORS = {
    Resource.WOOD: (34, 139, 34),
    Resource.BRICK: (139, 69, 19),
    Resource.SHEEP: (144, 238, 144),
    Resource.WHEAT: (255, 215, 0),
    Resource.ORE: (169, 169, 169),
    Resource.NONE: (255, 255, 204) # Desert
}

class Display:
    def __init__(self, board: Board):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Catan AI")
        self.board = board
        self.font = pygame.font.SysFont(None, 24)

    def draw_hex(self, x, y, resource, value):
        """Draw a single hexagon on the screen."""
        points = []
        for i in range(6):
            angle_deg = 60 * i
            angle_rad = math.pi / 180 * angle_deg
            points.append((x + HEX_SIZE * math.cos(angle_rad),
                           y + HEX_SIZE * math.sin(angle_rad)))
        
        pygame.draw.polygon(self.screen, RESOURCE_COLORS[resource], points)
        pygame.draw.polygon(self.screen, BLACK, points, 2) # Border

        # Draw the value
        if value > 0:
            text = self.font.render(str(value), True, BLACK)
            text_rect = text.get_rect(center=(x, y))
            self.screen.blit(text, text_rect)

    def run(self):
        """Main loop to run the display."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(WHITE)
            
            # For now, just draw the first hex at the center
            if self.board.hexes:
                first_hex = self.board.hexes[0]
                self.draw_hex(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, first_hex.resource, first_hex.value)

            pygame.display.flip()

        pygame.quit()
