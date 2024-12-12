from enum import Enum

with open("./input.txt") as file:
    lines = [l.removesuffix("\n") for l in file.readlines()]

visited_cells = [["" for c in l] for l in lines]

def get_value_at(row, col):
    if row < 0 or col < 0:
        return None
    try:
        return lines[row][col]
    except IndexError:
        return None

def get_size_of_region_starting_at(row: int, col: int) -> tuple[int, int, int]:
    area = 1
    perimeter = 0
    visited_cells[row][col] = "X"
    sides = 0

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i != j and i != -j:
                if get_value_at(row + i, col + j) == lines[row][col] and visited_cells[row + i][col + j] == "":
                    (a, p, s) = get_size_of_region_starting_at(row + i, col + j)
                    area += a
                    perimeter += p
                    sides += s
                elif get_value_at(row + i, col + j) != lines[row][col]:
                    perimeter += 1
    
    # In a polygon the number of sides is equal to the number of vertices
    if get_value_at(row - 1, col) != lines[row][col] and get_value_at(row, col - 1) != lines[row][col]:
        sides += 1
    if get_value_at(row - 1, col) != lines[row][col] and get_value_at(row, col + 1) != lines[row][col]:
        sides += 1
    if get_value_at(row + 1, col) != lines[row][col] and get_value_at(row, col - 1) != lines[row][col]:
        sides += 1
    if get_value_at(row + 1, col) != lines[row][col] and get_value_at(row, col + 1) != lines[row][col]:
        sides += 1
    if get_value_at(row - 1, col - 1) != lines[row][col] and get_value_at(row - 1, col) == lines[row][col] and get_value_at(row, col - 1) == lines[row][col]:
        sides += 1
    if get_value_at(row - 1, col + 1) != lines[row][col] and get_value_at(row - 1, col) == lines[row][col] and get_value_at(row, col + 1) == lines[row][col]:
        sides += 1
    if get_value_at(row + 1, col - 1) != lines[row][col] and get_value_at(row + 1, col) == lines[row][col] and get_value_at(row, col - 1) == lines[row][col]:
        sides += 1
    if get_value_at(row + 1, col + 1) != lines[row][col] and get_value_at(row + 1, col) == lines[row][col] and get_value_at(row, col + 1) == lines[row][col]:
        sides += 1
    
    return area, perimeter, sides


full_price = 0
discounted_price = 0
for row in range(len(lines)):
    for col in range(len(lines[row])):
        if visited_cells[row][col] == "":
            (area, perimeter, sides) = get_size_of_region_starting_at(row, col)
            full_price += area * perimeter
            discounted_price += area * sides

print(full_price)
print(discounted_price)