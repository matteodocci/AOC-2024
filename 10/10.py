with open("./input.txt") as file:
    lines = file.readlines()

topographic_map = [[int(char) for char in line.removesuffix("\n")] for line in lines]

def find_trailheads() -> tuple[int, int]:
    trailheads = []

    for row in range(len(topographic_map)):
        for col in range(len(topographic_map[0])):
            if topographic_map[row][col] == 0:
                trailheads.append((row, col))
    
    return trailheads

def is_value_in_position(row: int, col: int, value: int) -> bool:
    if row < 0 or col < 0:
        return False

    try:
        if topographic_map[row][col] == value:
            return True
    except:
        pass

    return False

def get_reachable_positions(row: int, col: int, value: int) -> set[tuple[int, int]]:
    next_positions = set()
    reachable_positions = set()

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i != j and i != -j and is_value_in_position(row + i, col + j, value):
                next_positions.add((row + i, col + j))
    
    if value == 9:
        return next_positions
    
    for (row, col) in next_positions:
        reachable_positions = reachable_positions.union(get_reachable_positions(row, col, value + 1))

    return reachable_positions

def get_rating(row: int, col: int, value: int) -> set[tuple[int, int]]:
    rating = 0
    next_positions = set()

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i != j and i != -j and is_value_in_position(row + i, col + j, value):
                next_positions.add((row + i, col + j))
    
    if value == 9:
        return len(next_positions)
    
    for (row, col) in next_positions:
        rating += get_rating(row, col, value + 1)

    return rating


score = 0
rating = 0
trailheads = find_trailheads()
for (row, col) in trailheads:
    score += len(get_reachable_positions(row, col, value=1))
    rating += get_rating(row, col, value=1)

print(score)
print(rating)