from networkx import eulerian_circuit
from settings import EXPAND_COLOR, FINISHED_COLOR, GOAL_COLOR, PATH_COLOR, REACHED_COLOR, SELECTED_COLOR, START_COLOR, UNBLOCKED_COLOR, Settings
from collections import deque
from queue import PriorityQueue
import pygame
import time
import random


class Algo:
    def __init__(self):
        self.start = None
        self.goals = []
        self.matrix = []

    def init_tracer(self):
        self.trace = [[]]

    def bfs(self, drawer):

        queue = deque()
        queue.append(self.start)
        while queue:
            c_cell = queue.popleft()
            self.select(c_cell)
            self.drawy(drawer)

            if self.check_goals(c_cell, drawer):
                self.drawy(drawer)
                return

            for cell in self.get_neighboor(c_cell):
                if self.is_free(cell):
                    self.expand(cell)
                    queue.append(cell)
                    cell.father = c_cell

            self.reached(c_cell)
            self.drawy(drawer)

    def dfs(self, drawer):

        stack = []
        stack.append(self.start)
        while stack:
            c_cell = stack.pop()
            self.select(c_cell)
            self.drawy(drawer)

            if self.check_goals(c_cell, drawer):
                self.drawy(drawer)
                return

            for cell in self.get_neighboor(c_cell):
                if self.is_free(cell):
                    self.expand(cell)
                    stack.append(cell)
                    cell.father = c_cell

            self.reached(c_cell)
            self.drawy(drawer)

    def a_star(self, drawer):
        pq = PriorityQueue()
        self.start.eval = 0
        pq.put((self.start))
        while not pq.empty():
            c_cell = pq.get()
            self.select(c_cell)
            self.drawy(drawer)

            if self.check_goals(c_cell, drawer):
                self.drawy(drawer)
                return

            for cell in self.get_neighboor(c_cell):
                if self.is_free(cell):
                    if (not self.is_expanded(cell) or cell.distance > c_cell.distance+1):
                        self.expand(cell)
                        cell.distance = c_cell.distance + cell.cost
                        cell.father = c_cell
                    # stack.append(cell)
                    cell.eval = self.eval_function(cell)
                    pq.put((cell))

            self.reached(c_cell)
            self.drawy(drawer)

    def heuristic(self, cell):
        return self.mannhattan_dis(cell)

    def mannhattan_dis(self, cell):
        # if self.goals:
        #     return abs(cell.row - self.goals[0].row) + abs(cell.col - self.goals[0].col)
        # return 0
        min_dis = 10000000000
        for goal in self.goals:
            min(min_dis, abs(cell.row -
                self.goals[0].row) + abs(cell.col - self.goals[0].col))

        return min_dis

    def euclidean_dis(self, cell):
        if self.goals:
            return ((cell.row - self.goals[0].row)**2 + (cell.col - self.goals[0].col)**2)**.5
        return 0

    def path_cost(self, cell):
        return cell.distance

    def eval_function(self, cell):
        return self.path_cost(cell) + self.heuristic(cell)

    def is_expanded(self, cell):
        return cell.color == EXPAND_COLOR

    def is_reached(self, cell):
        return cell.color == REACHED_COLOR

    def get_neighboor(self, cell):
        res = []
        pos_x, pos_y = cell.pos
        idx_diff = [(1, 0),  (0, 1), (-1, 0), (0, -1)]
        for i, j in idx_diff:
            c_cell = self.matrix[pos_x+i][pos_y+j]
            res.append(c_cell)

        return res

    def is_free(self, cell):
        return cell.color == UNBLOCKED_COLOR or cell.color == GOAL_COLOR or cell.color == FINISHED_COLOR

    def expand(self, cell):
        cell.color = EXPAND_COLOR

    def reached(self, cell):
        cell.color = REACHED_COLOR

    def select(self, cell):
        cell.color = SELECTED_COLOR

    def check_goals(self, cell, drawer):

        for goal in self.goals:
            if cell == goal:
                if not goal.is_finished():
                    goal.finished()
                    self.make_path(goal, drawer)
                    return True

        return False

    def pathing(self, cell):
        cell.color = PATH_COLOR

    def make_path(self, goal, drawer):
        trace = goal.father
        while trace.father != None:
            self.pathing(trace)
            self.drawy(drawer)

            trace = trace.father

    def run(self, drawer):
        # self.bfs(drawer)
        start_time = time.time()
        self.stochastic_hill_climbing(drawer)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Elapsed time:", elapsed_time, "seconds")

    def update(self):
        self.start.color = START_COLOR
        for goal in self.goals:
            goal.color = GOAL_COLOR

    def drawy(self, drawer):
        drawer()
        self.update()
        pygame.display.flip()

    def hill_climbing(self, drawer):
        current_cell = self.start
        while True:
            self.select(current_cell)
            self.drawy(drawer)

            if self.check_goals(current_cell, drawer):
                self.drawy(drawer)
                return

            next_best_cell = None
            for neighbor_cell in self.get_neighboor(current_cell):
                if (self.is_free(neighbor_cell) or neighbor_cell.color == SELECTED_COLOR) and self.heuristic(neighbor_cell) <= self.heuristic(current_cell):
                    next_best_cell = neighbor_cell
                    break

            if next_best_cell is None:
                break

            self.expand(next_best_cell)
            current_cell = next_best_cell

        self.reached(current_cell)
        self.drawy(drawer)

    def stochastic_hill_climbing(self, drawer):
        current_cell = self.start
        while True:
            self.select(current_cell)
            self.drawy(drawer)

            if self.check_goals(current_cell, drawer):
                self.drawy(drawer)

                break

            next_best_cells = []
            max_heuristic = float('-inf')
            for neighbor_cell in self.get_neighboor(current_cell):
                if (self.is_free(neighbor_cell) or neighbor_cell.color == SELECTED_COLOR):
                    neighbor_heuristic = self.heuristic(neighbor_cell)

                    if neighbor_heuristic > max_heuristic:
                        next_best_cells = [neighbor_cell]
                        max_heuristic = neighbor_heuristic
                    elif neighbor_heuristic == max_heuristic:
                        next_best_cells.append(neighbor_cell)

            if not next_best_cells:
                break

            next_cell = random.choice(next_best_cells)
            self.expand(next_cell)
            current_cell = next_cell

        self.reached(current_cell)
        self.drawy(drawer)
