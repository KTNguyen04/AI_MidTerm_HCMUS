
from numpy import block
import pygame
from cell import Cell
from settings import BLOCKED_COLOR, GOAL_COLOR, GRAY_C, START_COLOR, UNBLOCKED_COLOR, Settings
import random


class Grid:
    def __init__(self, s_v):
        self.cells = []
        self.rows = Settings.n_rows
        self.cols = Settings.n_cols

        self.window = s_v.window
        self.screen = s_v.screen
        self.make_cells()
        self.make_barrier()

    def make_cells(self):
        matrix = read_matrix_from_file("cost.txt")
        for x in range(self.rows):
            row = []
            for y in range(self.cols):
                cell = Cell(x, y)
                cell.cost = matrix[x][y]
                if cell.cost > 0:
                    cell.color = UNBLOCKED_COLOR
                elif cell.cost == -1:
                    cell.color = BLOCKED_COLOR
                elif cell.cost == 0:
                    cell.color = START_COLOR
                if cell.cost == 999:
                    cell.color = GOAL_COLOR

                row.append(cell)
            self.cells.append(row)

    def draw(self):

        for row in self.cells:
            for cell in row:
                cell.draw_cell(self.screen)
                cell.draw_cost(self.screen)

        self._draw_grid()

    def _draw_grid(self):
        for x in range(self.rows+1):
            pygame.draw.line(self.screen, GRAY_C, (self.window.left,
                             self.window.top+x*Settings.cell_height), (self.window.right, self.window.top+x*Settings.cell_height))

        for x in range(self.cols+1):
            pygame.draw.line(self.screen, GRAY_C, (self.window.left+x*Settings.cell_width,
                                                   self.window.top), (self.window.left+x*Settings.cell_width, self.window.bottom))

    def make_barrier(self):
        for row in self.cells:
            for cell in row:
                if self.check_barrier(cell.pos):
                    cell.blocked()

    def check_barrier(self, pos):
        pos_x = pos[0]
        pos_y = pos[1]
        return pos_x == 0 or pos_x == self.cols-1 or pos_y == 0 or pos_y == self.rows-1


def read_matrix_from_file(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            row = [int(x) for x in line.split()]
            matrix.append(row)
    return matrix
