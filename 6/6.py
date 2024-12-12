from mapTraversal import traverse

file = open("./input.txt")
lines = file.readlines()
file.close()

gameMap = [[c for c in line.removesuffix("\n")] for line in lines]

_, visitedPositions = traverse(gameMap)

print(len(visitedPositions))

# After some time I decided to resort to bruteforce, probably making some elf cry.
# After checking on Reddit it seems like everyone bruteforced this problem.

additionalObstacles = []

for count, position in enumerate(visitedPositions, start=1):
    if count % 100 == 0:
        print(f"{count}/{len(visitedPositions)}")

    x, y = position
    if gameMap[y][x] == ".":
        gameMap[y][x] = "#"
        loopDetected, _ = traverse(gameMap)
        gameMap[y][x] = "."
        
        if loopDetected:
            additionalObstacles.append(position)

print(len(additionalObstacles))