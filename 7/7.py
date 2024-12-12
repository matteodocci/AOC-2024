import re

def get_base_3_representation(num: int, length: int) -> str:
    q = num
    res = ""

    while True:
        r = q % 3
        q = q // 3
        res = str(r) + res
        
        if q == 0:
            return res.rjust(length, "0")

with open("./input.txt") as file:
    lines = file.readlines()

sum = 0

for line in lines:
    numbers = [int(num) for num in re.findall(r"(\d+)", line)]
    testValue = numbers[0]
    rest = numbers[1:]
    spaces = len(rest) - 1
    combinations = 3 ** spaces
    isPossible = False

    for i in range(combinations):
        base3Representation = get_base_3_representation(i, spaces)

        res = rest[0]
        for j, operator in enumerate(base3Representation, start=1):
            match operator:
                case "0":
                    res += rest[j]
                case "1":
                    res *= rest[j]
                case "2":
                    res = int(str(res) + str(rest[j]))
        
        if testValue == res:
            isPossible = True
            break
    
    if isPossible:
        sum += testValue

print(sum)