import string

with open('./inputs/day03.txt') as file:
    sum = 0
    i = 0
    group = []
    
    for line in file.readlines():
        line = line.strip()
        group.append(line)
        i = (i + 1) % 3
        
        if i == 0:
            duplicates = ''.join(set([c for c in group[0] if c in group[1] and c in group[2]]))
            if duplicates in string.ascii_uppercase:
                sum += 27 + string.ascii_uppercase.index(duplicates)
            else:
                sum += 1 + string.ascii_lowercase.index(str(duplicates[0]))

            group.clear()

    print("Sum: " + str(sum))