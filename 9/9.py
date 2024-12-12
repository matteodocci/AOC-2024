with open("./input.txt") as file:
    disk_map = file.read()

blocks = []

for i, value in enumerate(disk_map):
    if i % 2 == 0:
        blocks += [i // 2 for _ in range(int(value))]
    else:
        blocks += ["." for _ in range(int(value))]


blocks1 = blocks[:]
firstDotIdx = blocks1.index(".")
for i in range(len(blocks1)):
    # Speed up the search by continuing from the last position
    firstDotIdx = blocks1.index(".", firstDotIdx)
    if firstDotIdx >= len(blocks1) - i:
        break

    blockIdx = -1 - i
    if isinstance(blocks1[blockIdx], int):
        blocks1[firstDotIdx] = blocks1[blockIdx]
        blocks1[blockIdx] = "."
    
checksum1 = 0
for i, value in enumerate(blocks1):
    if not isinstance(value, int):
        break
    checksum1 += i * value

print(checksum1)


blocks2 = blocks[:]
currentValue = blocks2[-1]
fileSize = 0
for i in range(len(blocks2)):
    blockIdx = -1 - i

    if i % 1000 == 0:
        print(f"{i}/{len(blocks2)}")
        
    if isinstance(blocks2[blockIdx], int):
        if currentValue == blocks2[blockIdx]:
            fileSize += 1
        else:
            currentValue = blocks2[blockIdx]
            fileSize = 1

        if blockIdx - 1 > -len(blocks2) and blocks2[blockIdx - 1] != currentValue:
                freeSpaceSize = 0
                for j, value in enumerate(blocks2):
                    if j == len(blocks2) + blockIdx:
                        break
                    if value == ".":
                        freeSpaceSize += 1
                        if freeSpaceSize == fileSize:
                            for k in range(fileSize):
                                blocks2[blockIdx + k] = "."
                                blocks2[j - k] = currentValue
                            break
                    else:
                        freeSpaceSize = 0
    
checksum2 = 0
for i, value in enumerate(blocks2):
    if isinstance(value, int):
        checksum2 += i * value

print(checksum2)