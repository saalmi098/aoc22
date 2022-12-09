trees = []
sum = 0

with open("./inputs/day08-example.txt") as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    trees.append([int(c) for c in line])

sum = len(trees[0] * 2) + (len(trees) * 2 - 4)

for row, r in enumerate(trees):

    if row == 0 or row == len(trees) - 1:
        continue

    for col, height in enumerate(r):
        
        if col == 0 or col == len(r) - 1:
            continue

        vis_top = True
        vis_bot = True
        vis_left = True
        vis_right = True

        for i in range(len(trees)):
            # top to bottom
            val = trees[i][col]

            if val >= height:
                if i < row:
                    vis_top = False
                elif i > row:
                    vis_bot = False

        for j in range(len(r)):
            # left to right
            val = trees[row][j]

            if val >= height:
                if j < col:
                    vis_left = False
                elif j > col:
                    vis_right = False
        
        if vis_top or vis_bot or vis_left or vis_right:
            sum += 1

print(sum)