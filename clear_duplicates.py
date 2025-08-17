import json
import sys


def rotate(board):
    return [list(row[::-1]) for row in zip(*board)]


def mirror_x(board):
    return board[::-1]


def get_hash(board):
    a = board
    b = rotate(a)
    c = rotate(b)
    d = rotate(c)

    x = mirror_x(board)
    y = rotate(x)
    z = rotate(y)
    w = rotate(z)
    return json.dumps(sorted([a, b, c, d, x, y, z, w]))


solutions_file = sys.argv[1]


solutions = []
with open(solutions_file, "r") as sf:
    for l in sf.readlines():
        if not l:
            continue
        solutions.append(json.loads(l))

unique_solutions = {}
for s in solutions:
    unique_solutions[get_hash(s)] = s

print(len(solutions), len(unique_solutions))

with open("all_solutions.json", "a") as alls:
    for s in unique_solutions.values():
        alls.write(f"{json.dumps(s)}\n")
