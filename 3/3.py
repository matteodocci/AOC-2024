import re

file = open("./input.txt")
text = file.read()
file.close()

matches1 = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", text)

res1 = 0
for match in matches1:
    res1 += int(match[0]) * int(match[1])

print(res1)

text2 = re.sub(r"don't\(\).*?[\s\S]*?.*?(?:do\(\)|$)", "", text)

matches2 = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", text2)

res2 = 0
for match in matches2:
    res2 += int(match[0]) * int(match[1])

print(res2)