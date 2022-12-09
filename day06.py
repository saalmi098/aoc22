with open("./inputs/day06.txt") as file:
    for line in file.readlines():
        line = line.strip()
        
        for i in range(4, len(input)):
            range = input[i-4:i]

            if len(set(range)) == len(range):
                print(i, range)
                break