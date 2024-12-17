from enum import Enum
from queue import PriorityQueue
from collections import deque
import itertools

class Direction(Enum):
    NORTH = 0,
    EAST = 1,
    SOUTH = 2,
    WEST = 3

def reconstruct_path(came_from, current):
    path = deque()
    path.appendleft(current)

    while current in came_from:
        current = came_from[current]
        path.appendleft(current)

    return path

def h(a, b):
    y1, x1 = a
    y2, x2 = b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star(maze: list[str], start: tuple[int, int], end: tuple[int, int]):
    # https://stackoverflow.com/a/40205720
    counter = itertools.count()

    frontier = PriorityQueue()
    frontier.put((0, next(counter), { "row": start[0], "col": start[1], "points": 0, "direction": Direction.EAST }))
    came_from = { start: None }
    g = { start: 0 }

    while not frontier.empty():
        _, _, current = frontier.get()
        row = current["row"]
        col = current["col"]

        if row == end[0] and col == end[1]:
            return reconstruct_path(came_from, end), g

        neighbors = []

        if current["direction"] != Direction.SOUTH and maze[row - 1][col] != "#":
            points = 1 if current["direction"] == Direction.NORTH else 1001
            neighbors.append({ "row": row - 1, "col": col, "points": points, "direction": Direction.NORTH })

        if current["direction"] != Direction.WEST and maze[row][col + 1] != "#":
            points = 1 if current["direction"] == Direction.EAST else 1001
            neighbors.append({ "row": row, "col": col + 1, "points": points, "direction": Direction.EAST })
        
        if current["direction"] != Direction.NORTH and maze[row + 1][col] != "#":
            points = 1 if current["direction"] == Direction.SOUTH else 1001
            neighbors.append({ "row": row + 1, "col": col, "points": points, "direction": Direction.SOUTH })

        if current["direction"] != Direction.EAST and maze[row][col - 1] != "#":
            points = 1 if current["direction"] == Direction.WEST else 1001
            neighbors.append({ "row": row, "col": col - 1, "points": points, "direction": Direction.WEST })

        for neighbor in neighbors:
            neighbor_position = (neighbor["row"], neighbor["col"])
            g_neighbor = g[(row, col)] + neighbor["points"]

            if neighbor_position not in g or g_neighbor < g[neighbor_position]:
                g[neighbor_position] = g_neighbor
                prio = g_neighbor + h(neighbor_position, end)
                frontier.put((prio, next(counter), { "row": neighbor["row"], "col": neighbor["col"], "points": g_neighbor, "direction": neighbor["direction"] }))
                came_from[neighbor_position] = (row, col)
        
    return None

with open("./input.txt") as file:
    maze = file.readlines()

for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == "S":
            start = (i, j)
        if maze[i][j] == "E":
            end = (i, j)

path, g = a_star(maze, start, end)

print(g[end])