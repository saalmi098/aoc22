import string

with open('./inputs/day03.txt') as file:
    sum = 0
    for line in file.readlines():
        line = line.strip()
        half1 = line[:round(len(line) / 2)]
        half2 = line[round(len(line) / 2):]
        
        duplicates = ''.join(set([c for c in half1 if c in half2]))

        if duplicates in string.ascii_uppercase:
            sum += 27 + string.ascii_uppercase.index(duplicates)
        else:
            sum += 1 + string.ascii_lowercase.index(str(duplicates[0]))

    print("Sum: " + str(sum))