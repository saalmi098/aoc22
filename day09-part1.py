import enum

class Direction(enum.Enum):
    Up = "U"
    Down = "D"
    Left = "L"
    Right = "R"

class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + ", " + str(self.y)
    
    def move(self, dir: Direction):
        assert dir != ""
        match dir:
            case Direction.Up: self.y -= 1
            case Direction.Down: self.y += 1
            case Direction.Left: self.x -= 1
            case Direction.Right: self.x += 1

with open("./inputs/day09.txt") as file:
    moves = [line.strip().split() for line in file]

pos_head = Position(0, 0)
pos_tail = Position(0, 0)
visited = []
min_x, max_x, min_y, max_y = 0, 0, 0, 0

def printField():
    global min_x, max_x, min_y, max_y
    min_x = min(min_x, pos_head.x, pos_tail.x)
    max_x = max(max_x, pos_head.x, pos_tail.x)
    min_y = min(min_y, pos_head.y, pos_tail.y)
    max_y = max(max_y, pos_head.y, pos_tail.y)

    print("\n")
    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            char = "."
            if x == pos_tail.x and y == pos_tail.y:
                char = "T"
            if x == pos_head.x and y == pos_head.y:
                char = "H"
            print(char, end="")
        print()

for move in moves:
    dir = Direction(move[0])
    steps = int(move[1])

    for i in range(steps):
        pos_head.move(dir)
        dir_tail: Direction

        if pos_head.y == pos_tail.y:
            # same row
            if abs(pos_head.x - pos_tail.x) >= 2:
                dir_tail = Direction.Right if pos_tail.x < pos_head.x else Direction.Left
                pos_tail.move(dir_tail)

        elif pos_head.x == pos_tail.x:
            # same column
            if abs(pos_head.y - pos_tail.y) >= 2:
                dir_tail = Direction.Down if pos_tail.y < pos_head.y else Direction.Up
                pos_tail.move(dir_tail)

        elif (abs(pos_head.y - pos_tail.y) == 2 and abs(pos_head.x - pos_tail.x) == 1) \
            or (abs(pos_head.y - pos_tail.y) == 1 and abs(pos_head.x - pos_tail.x) == 2):
            # diagonal
            dir_tail = Direction.Right if pos_tail.x < pos_head.x else Direction.Left
            pos_tail.move(dir_tail)
            dir_tail = Direction.Down if pos_tail.y < pos_head.y else Direction.Up
            pos_tail.move(dir_tail)

        #printField()
        visited.append((pos_tail.x, pos_tail.y))

print("count: " + str(len(set(visited))))