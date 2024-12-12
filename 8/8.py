class Antenna:
    def __init__(self, freq: str, row_idx: int, col_idx: int):
        self.freq = freq
        self.row_idx = row_idx
        self.col_idx = col_idx

def position_in_map(game_map: list[str], antinode: set[int, int]):
    return (antinode[0] >= 0 
            and antinode[0] < len(game_map)
            and antinode[1] >= 0 
            and antinode[1] < len(game_map[0]))

with open("./input.txt") as file:
    game_map = [l.rstrip() for l in file.readlines()]

antennas: list[Antenna] = list()

for row_idx, row in enumerate(game_map):
    for col_idx, char in enumerate(row):
        if char != ".":
            antennas.append(Antenna(char, row_idx, col_idx))

antinodes = set()

for i, antenna1 in enumerate(antennas):
    antenna1: Antenna

    antinodes.add((antenna1.row_idx, antenna1.col_idx))

    for j, antenna2 in enumerate(antennas[i+1:]):
        antenna2: Antenna

        if antenna1.freq == antenna2.freq:
            dist_x = antenna1.col_idx - antenna2.col_idx
            dist_y = antenna1.row_idx - antenna2.row_idx

            prev1 = (antenna1.row_idx, antenna1.col_idx)
            prev2 = (antenna2.row_idx, antenna2.col_idx)

            while True:
                antinode1 = (prev1[0] + dist_y, prev1[1] + dist_x)
                antinode2 = (prev2[0] - dist_y, prev2[1] - dist_x)

                atLeastOneInMap = False

                if position_in_map(game_map, antinode1):
                    antinodes.add(antinode1)
                    prev1 = antinode1
                    atLeastOneInMap = True

                if position_in_map(game_map, antinode2):
                    antinodes.add(antinode2)
                    prev2 = antinode2
                    atLeastOneInMap = True

                if not atLeastOneInMap:
                    break

print(len(antinodes))