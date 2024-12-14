import re
import os
import time

width = 101
height = 103
robots = []
q1 = 0
q2 = 0
q3 = 0
q4 = 0

with open("./input.txt") as file:
    lines = file.readlines()

for line in lines:
    values = [int(n) for n in re.findall(r"(-?\d+)", line)]
    robots.append(dict(zip(["px", "py", "vx", "vy"], values)))

for robot in robots:
    x = (robot["vx"] * 100 + robot["px"]) % width
    y = (robot["vy"] * 100 + robot["py"]) % height

    if x < width // 2 and y < height // 2:
        q1 += 1
    if x >= width // 2 + 1 and y < height // 2:
        q2 += 1
    if x >= width // 2 + 1 and y >= height // 2 + 1:
        q3 += 1
    if x < width // 2 and y >= height // 2 + 1:
        q4 += 1

print(q1 * q2 * q3 * q4)


for t in range(1_000_000):
    # I learned the hard way that this code
    # matrix = [[0] * width] * height
    # matrix[0][0] = 1
    # produces a matrix of zeros, but sets ALL the first column to 1.
    # Every row is a pointer to the same data.
    matrix = [[" "] * width for _ in range(height)]

    for robot in robots:
        x = (robot["vx"] * t + robot["px"]) % width
        y = (robot["vy"] * t + robot["py"]) % height

        matrix[y][x] = "*"

    for row in matrix:
        if ("".join(row)).find("******") > -1:
            os.system("cls")
            print(f"t = {t}")
            for row in matrix:
                print("".join(row))

            time.sleep(1)
            break