def horizontal(lines: list[str], i: int, j: int) -> str:
    return lines[i][j:j+4]

def vertical(lines: list[str], i: int, j: int) -> str:
    return "".join([line[j] for line in lines[i:i+4]])

def tl_to_br(lines: list[str], i: int, j: int) -> str:
    s = ""
    for k in range(0, 4):
        if len(lines) == i + k or len(lines[i+k]) == j + k:
            break
        s += lines[i+k][j+k]
    return s

def tr_to_bl(lines: list[str], i: int, j: int) -> str:
    s = ""
    for k in range(0, 4):
        if len(lines) == i + k or j - k < 0:
            break
        s += lines[i+k][j-k]
    return s

file = open("./input.txt")
lines = file.readlines()
file.close()

lines = [line.removesuffix("\n") for line in lines]
word = "XMAS"

count1 = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if horizontal(lines, i, j) == word:
            count1 += 1
        if horizontal(lines, i, j) == word[::-1]:
            count1 += 1
        if vertical(lines, i, j) == word:
            count1 += 1
        if vertical(lines, i, j) == word[::-1]:
            count1 += 1
        if tl_to_br(lines, i, j) == word:
            count1 += 1
        if tl_to_br(lines, i, j) == word[::-1]:
            count1 += 1
        if tr_to_bl(lines, i, j) == word:
            count1 += 1
        if tr_to_bl(lines, i, j) == word[::-1]:
            count1 += 1

print(count1)

count2 = 0
for i in range(1, len(lines) - 1):
    for j in range(1, len(lines[i]) - 1):
        d1 = lines[i-1][j-1] + lines[i][j] + lines[i+1][j+1]
        d2 = lines[i-1][j+1] + lines[i][j] + lines[i+1][j-1]

        if (d1 == "MAS" or d1 == "SAM") and (d2 == "MAS" or d2 == "SAM"):
            count2 += 1

print(count2)