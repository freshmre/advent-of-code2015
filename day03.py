santa = [0, 0]
turn = 0

houses = set()

moves = open("inp.txt").read().strip()

moves_map = {
    '^': 1j,
    'v': -1j,
    '>': 1,
    '<': -1,
}
for move in moves:
    houses.add(santa[turn])
    santa[turn] += moves_map[move]
    turn = not turn

print(len(houses))
    