import enum

class Direction(enum.Enum):
    Up = "U"
    Down = "D"
    Left = "L"
    Right = "R"

class Position:
    def __init__(self, id: str, x: int, y: int):
        self.id = id
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + ", " + str(self.y)
    
    def move(self, dir: Direction):
        match dir:
            case Direction.Up: self.y -= 1
            case Direction.Down: self.y += 1
            case Direction.Left: self.x -= 1
            case Direction.Right: self.x += 1

    def get_id(self):
        return self.id

with open("./inputs/day09.txt") as file:
    moves = [line.strip().split() for line in file]

pos = []
visited = []
for i in range(10):
    id = "H" if i == 0 else str(i)
    pos.append(Position(id, 0, 0))

def printField():
    min_x, max_x, min_y, max_y = 0, 6, -4, 1

    print("\n")
    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            char = "."
            for t in range(len(pos)):
                if x == pos[t].x and y == pos[t].y:
                    char = pos[t].id
                    break
            print(char, end="")
        print()

for move in moves:
    dir = Direction(move[0])
    steps = int(move[1])

    for i in range(steps):
        pos[0].move(dir) # move head
        dir_tail: Direction

        for t in range(1, len(pos)):
            pos_current = pos[t]
            pos_prior = pos[t - 1]

            if pos_prior.y == pos_current.y:
                # same row
                if abs(pos_prior.x - pos_current.x) >= 2:
                    dir_tail = Direction.Right if pos_current.x < pos_prior.x else Direction.Left
                    pos_current.move(dir_tail)

            elif pos_prior.x == pos_current.x:
                # same column
                if abs(pos_prior.y - pos_current.y) >= 2:
                    dir_tail = Direction.Down if pos_current.y < pos_prior.y else Direction.Up
                    pos_current.move(dir_tail)

            elif (abs(pos_prior.y - pos_current.y) == 2 and abs(pos_prior.x - pos_current.x) == 1) \
                 or (abs(pos_prior.y - pos_current.y) == 1 and abs(pos_prior.x - pos_current.x) == 2) \
                    or (abs(pos_prior.y - pos_current.y) == 2 and abs(pos_prior.x - pos_current.x) == 2):
                # diagonal
                dir_tail = Direction.Right if pos_current.x < pos_prior.x else Direction.Left
                pos_current.move(dir_tail)
                dir_tail = Direction.Down if pos_current.y < pos_prior.y else Direction.Up
                pos_current.move(dir_tail)

            if t == len(pos) - 1:
                visited.append((pos_current.x, pos_current.y))

        #printField()
        #input("Press Enter to step further")

print("count: " + str(len(set(visited))))