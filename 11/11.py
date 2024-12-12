import functools

@functools.cache
def get_length(stone: str, n: int) -> int:
    new_stones = []

    if stone == "0":
        new_stones.append("1")
    elif len(stone) % 2 == 0:
        middle = len(stone) // 2
        new_stones.extend([stone[:middle], str(int(stone[middle:]))])
    else:
        new_stones.append(str(int(stone) * 2024))

    if (n == 1):
        return len(new_stones)
    
    length = 0
    for new_stone in new_stones:
        length += get_length(new_stone, n - 1)
    return length


with open("./input.txt") as file:
    stones = file.read().split()

length = 0
for stone in stones:
    length += get_length(stone, 75)

print(length)