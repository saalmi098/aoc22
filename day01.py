with open('./inputs/day01.txt') as file:
    lines = [line for line in file]

calories = [0]
i = 0

for line in lines:
    if line == "\n":
        i += 1
        calories.append(0)
        continue
    
    calories[i] += int(line)

#print(max(calories)) Part A
top3 = sorted(calories, reverse=True)[0:3]
print(sum(top3))