file = open("./input.txt")
lines = file.readlines()
file.close()

a = list()
b = list()
while len(lines) > 0:
    line = lines.pop()
    parts = line.split("   ")
    a.append(int(parts[0]))
    b.append(int(parts[1]))

a.sort()
b.sort()

diff = 0
similarity = 0
for i in range(len(a)):
    diff += abs(a[i] - b[i])
    similarity += a[i] * b.count(a[i])

print(diff)
print(similarity)