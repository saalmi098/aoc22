trees = []
scores = []

with open("./inputs/day08-example.txt") as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    trees.append([int(c) for c in line])

for row, r in enumerate(trees):

    if row == 0 or row == len(trees) - 1:
        continue

    for col, height in enumerate(r):
        
        if col == 0 or col == len(r) - 1:
            continue

        loop_top = list(reversed(range(row)))
        loop_bottom = list(range(row + 1, len(trees)))
        loop_left = list(reversed(range(col)))
        loop_right = list(range(col + 1, len(r)))
        count_top, count_bottom, count_left, count_right = 0, 0, 0, 0

        for q in loop_top:
            count_top += 1
            val = trees[q][col]

            if val >= height:
                break

        for i in loop_bottom:
            count_bottom += 1
            val = trees[i][col]

            if val >= height:
                break

        for z in loop_left:
            count_left += 1
            val = trees[row][z]

            if val >= height:
                break

        for x in loop_right:
            count_right += 1
            val = trees[row][x]

            if val >= height:
                break

        scores.append(count_top * count_bottom * count_left * count_right)

print(max(scores))