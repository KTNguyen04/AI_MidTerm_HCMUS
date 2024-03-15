import pygame
from pygame.sprite import Sprite
from settings import BLOCKED_COLOR, GOAL_COLOR, START_COLOR, UNBLOCKED_COLOR, WHITE_C, Settings


class Cell():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.width = Settings.cell_width
        self.height = Settings.cell_height
        self.x = col*self.width + Settings.left_margin
        self.y = row*self.height + Settings.top_bot_margin
        self.pos = (self.row, self.col)
        self.color = WHITE_C
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.goaled = False
        self.father = None

        self.distance = 0
        self.eval = 0

        self.cost = 0

    def draw_cell(self, suf):
        pygame.draw.rect(suf, self.color, self.rect)

    def blocked(self):
        self.color = BLOCKED_COLOR

    def unblocked(self):
        self.color = UNBLOCKED_COLOR

    def make_start(self):
        self.color = START_COLOR

    def make_goal(self):
        self.color = GOAL_COLOR

    def get_rect(self):
        return self.rect

    def is_blocked(self):
        return self.color == BLOCKED_COLOR

    def is_start(self):
        return self.color == START_COLOR

    def is_goal(self):
        return self.color == GOAL_COLOR

    def is_finished(self):
        return self.goaled

    def finished(self):
        self.goaled = True

    def __lt__(self, other_c):
        return self.eval < other_c.eval

    def draw_cost(self, suf):
        # Create a font object
        # You can adjust the font size as needed
        font = pygame.font.Font(None, 24)

        # Render the cost text
        # Render cost as black color
        cost_text = font.render(str(self.cost), True, (0, 0, 0))

        # Get the text rectangle
        text_rect = cost_text.get_rect()

        # Set the text rectangle's center to the cell rectangle's center
        text_rect.center = self.rect.center

        # Blit (draw) the cost text onto the surface
        suf.blit(cost_text, text_rect)
