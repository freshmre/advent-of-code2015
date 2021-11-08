import re

with open("inp.txt", "r") as f:
    inp = f.read().splitlines()

class reindeer:
    def __init__(self, speed, active_t, rest_t):
        self.speed = speed
        self.active_t = active_t
        self.rest_t = rest_t
        self.timer = active_t
        self.dist = 0
        self.score = 0
        self.flying = True

    def step(self):
        if self.flying:
            self.dist += self.speed

        self.timer -= 1
        if not self.timer:
            if self.flying:
                self.timer = self.rest_t
            else:
                self.timer = self.active_t

            self.flying = not self.flying

furthest = 0
time = 2503
deer_lst = []

for deer_specs in inp:
    matches = re.match(r".*?(\d+).*?(\d+).*?(\d+)", deer_specs).groups()

    speed, active_t, rest_t = int(matches[0]), int(matches[1]), int(matches[2])
    new_deer = reindeer(speed, active_t, rest_t)
    deer_lst.append(new_deer)

for _ in range(time):
    for deer in deer_lst:
        deer.step()
        if deer.dist > furthest:
            furthest = deer.dist

    for deer in deer_lst:
        if deer.dist == furthest:
            deer.score += 1

print(max(deer.dist for deer in deer_lst))
print(max(deer.score for deer in deer_lst))
