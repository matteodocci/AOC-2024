import re

class Machine:
    def __init__(self, x1, y1, x2, y2, x_prize, y_prize):
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)
        self.x_prize = int(x_prize) + 10000000000000
        self.y_prize = int(y_prize) + 10000000000000


with open("./input.txt") as file:
    text = file.read()

machine_descriptions = text.split("\n\n")
pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"
machines: list[Machine] = []

for desc in machine_descriptions:
    values = re.findall(pattern, desc)[0]
    machines.append(Machine(*values))

tokens_a = 3
tokens_b = 1
tokens_tot = 0

for m in machines:
    n_press_b = (m.x1 * m.y_prize - m.x_prize * m.y1) / (m.x1 * m.y2 - m.x2 * m.y1)
    n_press_a = (m.x_prize - m.x2 * n_press_b) / m.x1
    if n_press_a.is_integer() and n_press_a >= 0 and n_press_b.is_integer() and n_press_b >= 0:
        tokens_tot += n_press_a * tokens_a + n_press_b * tokens_b

print(tokens_tot)