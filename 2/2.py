file = open("./input.txt")
lines = file.readlines()
file.close()

countSafe = 0
countDampened = 0
for line in lines:
    previous = None
    wasAscending = None
    isAscending = None
    isSafe = True
    problems = 0
    words = line.split()

    for word in words:
        number = int(word)

        if id(word) != id(words[0]):
            distance = abs(previous - number)
            isAscending = number > previous

            if distance < 1 or distance > 3 or (id(word) != id(words[1]) and isAscending != wasAscending):
                isSafe = False
                problems += 1
        
        previous = number
        wasAscending = isAscending

    if isSafe:
        countSafe += 1
    if problems == 1:
        countDampened += 1


print(str(countSafe))
print(str(countSafe + countDampened))