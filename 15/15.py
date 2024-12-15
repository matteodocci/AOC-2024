def can_move_large_box_vertically(row, col, direction, warehouse):
    new_row = row + (1 if direction == "v" else - 1)
    other_side_col = col + (1 if warehouse[row][col] == "[" else - 1)

    if warehouse[new_row][col] == "#" or warehouse[new_row][other_side_col] == "#":
        return False
    
    if warehouse[new_row][col] in "[]" and not can_move_large_box_vertically(new_row, col, direction, warehouse):
        return False

    if warehouse[new_row][other_side_col] in "[]" and not can_move_large_box_vertically(new_row, other_side_col, direction, warehouse):
        return False
    
    return True

def move_large_box_vertically(row, col, direction, warehouse):
    new_row = row + (1 if direction == "v" else - 1)
    other_side_col = col + (1 if warehouse[row][col] == "[" else - 1)
    
    if warehouse[new_row][col] in "[]":
        move_large_box_vertically(new_row, col, direction, warehouse)

    if warehouse[new_row][other_side_col] in "[]":
        move_large_box_vertically(new_row, other_side_col, direction, warehouse)

    warehouse[new_row][col] = warehouse[row][col]
    warehouse[row][col] = "."
    
    warehouse[new_row][other_side_col] = warehouse[row][other_side_col]
    warehouse[row][other_side_col] = "."

    return new_row, col

def move_large_box(new_row, new_col, direction, warehouse):
    if direction in "^v" and not can_move_large_box_vertically(new_row, new_col, direction, warehouse):
        return new_row, new_col
    
    if direction in "^v":
        return move_large_box_vertically(new_row, new_col, direction, warehouse)
    
    return move(new_row, new_col, direction, warehouse)

def move(row, col, direction, warehouse):
    new_row = row
    new_col = col

    match direction:
        case "^":
            new_row -= 1
        case ">":
            new_col += 1
        case "<":
            new_col -= 1
        case "v":
            new_row += 1

    match warehouse[new_row][new_col]:
        case ".":
            warehouse[new_row][new_col] = warehouse[row][col]
            warehouse[row][col] = "."
        case "O":
            new_box_row, new_box_col = move(new_row, new_col, direction, warehouse)
            if (new_box_row, new_box_col) != (new_row, new_col):
                move(row, col, direction, warehouse)
            else:
               new_row = row
               new_col = col
        case "#":
            new_row = row
            new_col = col
        case "[" | "]":
            new_box_row, new_box_col = move_large_box(new_row, new_col, direction, warehouse)
            if (new_box_row, new_box_col) != (new_row, new_col):
                move(row, col, direction, warehouse)
            else:
               new_row = row
               new_col = col

    return new_row, new_col


with open("./input.txt") as file:
    text = file.read()

warehouse_text, directions = text.split("\n\n")

warehouse1 = [[c for c in line] for line in warehouse_text.split("\n")]
directions = directions.replace("\n", "")
warehouse1_initial_state = [row[:] for row in warehouse1]

for i, row in enumerate(warehouse1):
    for j, char in enumerate(row):
        if char == "@":
            position1 = { "row": i, "col": j }
            break

for direction in directions:
    position1["row"], position1["col"] = move(position1["row"], position1["col"], direction, warehouse1)
   
coords_sum_1 = 0
for i, row in enumerate(warehouse1):
    for j, char in enumerate(row):
        if char == "O":
            coords_sum_1 += i * 100 + j

print(coords_sum_1)


warehouse2 = []
for row in warehouse1_initial_state:
    row2 = []
    for char in row:
        match char:
            case "#":
                row2 += ["#", "#"]
            case ".":
                row2 += [".", "."]
            case "@":
                row2 += ["@", "."]
            case "O":
                row2 += ["[", "]"]
    warehouse2.append(row2)

for i, row in enumerate(warehouse2):
    for j, char in enumerate(row):
        if char == "@":
            position2 = { "row": i, "col": j }
            break

for direction in directions:
    position2["row"], position2["col"] = move(position2["row"], position2["col"], direction, warehouse2)
 
coords_sum_2 = 0
for i, row in enumerate(warehouse2):
    for j, char in enumerate(row):
        if char == "[":
            coords_sum_2 += i * 100 + j

print(coords_sum_2)