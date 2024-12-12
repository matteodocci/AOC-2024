from enum import Enum

class Direction(Enum):
    UP = 0,
    RIGHT = 1,
    DOWN = 2,
    LEFT = 3


def traverse(gameMap):
    visitedPositions = set()
    # Using a set instead of a list significantly improved performance
    stepsTaken = set()
    loopDetected = False
    direction = Direction.UP
    position = ()

    for i in range(len(gameMap)):
        for j in range(len(gameMap[i])):
            if gameMap[i][j] == "^":
                position = (j, i)
                break

    visitedPositions.add(position)
    stepsTaken.add((position, direction))

    while True:
        x = position[0]
        y = position[1]

        match direction:
            case Direction.UP:
                newY = y - 1
                if newY < 0:
                    break
                if gameMap[newY][x] == "#":
                    direction = Direction.RIGHT
                else:
                    position = (x, newY)
                    visitedPositions.add(position)
                    if (position, direction) in stepsTaken:
                        loopDetected = True
                        break
                    stepsTaken.add((position, direction))

            case Direction.RIGHT:
                newX = x + 1
                if newX == len(gameMap[y]):
                    break
                if gameMap[y][newX] == "#":
                    direction = Direction.DOWN
                else:
                    position = (newX, y)
                    visitedPositions.add(position)
                    if (position, direction) in stepsTaken:
                        loopDetected = True
                        break
                    stepsTaken.add((position, direction))

            case Direction.DOWN:
                newY = y + 1
                if newY == len(gameMap):
                    break
                if gameMap[newY][x] == "#":
                    direction = Direction.LEFT
                else:
                    position = (x, newY)
                    visitedPositions.add(position)
                    if (position, direction) in stepsTaken:
                        loopDetected = True
                        break
                    stepsTaken.add((position, direction))

            case Direction.LEFT:
                newX = x - 1
                if newX < 0:
                    break
                if gameMap[y][newX] == "#":
                    direction = Direction.UP
                else:
                    position = (newX, y)
                    visitedPositions.add(position)
                    if (position, direction) in stepsTaken:
                        loopDetected = True
                        break
                    stepsTaken.add((position, direction))

    return loopDetected, visitedPositions