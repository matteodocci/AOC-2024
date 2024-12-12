import re

file = open("./input.txt")
text = file.read()
file.close()

parts = text.split("\n\n")

rules = [[int(x),int(y)] for x, y in re.findall(r"(\d+)\|(\d+)", parts[0])]

lines = parts[1].split("\n")
updates = [[int(n) for n in line.split(",")] for line in lines]

validUpdates = []
invalidUpdates = []
for update in updates:
    isValid = True

    for i in range(len(update)):
        prev = update[:i]
        succ = update[i+1:]

        for prevNum in prev:
            if rules.count([update[i], prevNum]):
                isValid = False
                break
        for succNum in succ:
            if rules.count([succNum, update[i]]):
                isValid = False
                break
        if isValid == False:
            break

    if isValid:
        validUpdates.append(update)
    else:
        invalidUpdates.append(update)

sum = 0
for update in validUpdates:
    sum += update[len(update)//2]
print(sum)

reorderedUpdates = []
for update in invalidUpdates:    
    reorderedUpdate = update[:]

    while True:
        changed = False

        for i in range(len(reorderedUpdate)):
            for j in range(i+1, len(reorderedUpdate)):
                if rules.count([reorderedUpdate[j], reorderedUpdate[i]]) == 1:
                    tmp = reorderedUpdate[i]
                    reorderedUpdate[i] = reorderedUpdate[j]
                    reorderedUpdate[j] = tmp
                    changed = True

        if changed == False:
            break
    
    reorderedUpdates.append(reorderedUpdate)

sum = 0
for update in reorderedUpdates:
    sum += update[len(update)//2]
print(sum)