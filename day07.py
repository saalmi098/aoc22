dirs = {}
currDir = '/'
dirs[currDir] = 0

def get_2nd_last_index(s, c) -> int:
    return s[:s.rfind(c)].rfind(c)

with open("./inputs/day07.txt") as file:
    for line in file.readlines():
        line = line.strip()

        if line.startswith("$"):
            # command
            line = line.replace("$ ", "")

            if line.startswith("cd "):
                dir = line.split()[1]
                if dir == "..":
                    currDir = currDir[0:get_2nd_last_index(currDir, "/") + 1]
                elif dir != "/":
                    currDir += dir + "/"

        else:
            # directory or file
            name = line.split()[1]
            if line.startswith("dir"):
                assert not dirs.__contains__(currDir + name + "/")
                dirs[currDir + name  + "/"] = 0
            else:
                # add file size to directory sizes
                to_update = currDir.rstrip("/").split("/")
                for x in to_update:
                    if x == "":
                        pathBuilder = "/"
                    else:
                        pathBuilder += x + "/"

                    dirs[pathBuilder] += int(line.split()[0])

# part 1
sum = 0
for name, size in dirs.items():
    if (size <= 100000):
        sum += size
        #print(name + "\t" + str(size))

print("Sum: " + str(sum))

# part 2
unused_space = 70000000 - dirs["/"]
needed_space = 30000000 - unused_space
larger_than_root = min([size for size in dirs.values() if size >= needed_space])
print(larger_than_root)