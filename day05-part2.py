stacks = []

class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)
    
    def pop(self) -> int:
        return self.items.pop()

    def __str__(self):
        return ''.join(reversed(self.items))

    def count(self) -> int:
        return len(self.items)

with open('./inputs/day05.txt') as file:
    all_lines = [line.rstrip() for line in file]
    matrix_orig = [line for line in all_lines if line.strip().startswith("[")]
    moves = [line.replace("move ", "").replace(" from", "").replace(" to", "") for line in all_lines if line.strip().startswith("move")]

    for i in range(0, 9):
        stacks.append(Stack())

    for line in reversed(matrix_orig):
        r, i = 0, 0
        while (r < len(line)):
            if (line[r:r+4].strip() != ""):
                stacks[i].push(line[r:r+4].replace("[", "").replace("]", "").strip())
            r += 4
            i += 1
    
    for move in moves:
        count, source, dest = map(int, move.split(' '))
        source -= 1
        dest -= 1

        i = 0
        to_push = []
        while (i < count):
            assert stacks[source].count() > 0
            to_push.append(stacks[source].pop())
            i += 1
        
        for x in reversed(to_push):
            stacks[dest].push(x)

    res = ""
    for stack in stacks:
        if stack.__count__() > 0:
            res += str(stack.pop())
    print(res)