import string

with open('./inputs/day04.txt') as file:
    count = 0
    for line in file.readlines():
        s1, s2 = line.strip().split(',')

        section1 = tuple(map(int, s1.split("-")))
        section2 = tuple(map(int, s2.split("-")))

        # part 1
        #if (section1[0] >= section2[0] and section1[1] <= section2[1]) or (section2[0] >= section1[0] and section2[1] <= section1[1]):
        #    count += 1

        # part 2
        range1 = range(section1[0], section1[1] + 1)
        range2 = range(section2[0], section2[1] + 1)

        commonSections = [i for i in range1 if i in range2]
        if len(commonSections) > 0:
            count += 1

    print(count)