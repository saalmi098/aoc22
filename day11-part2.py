from functools import reduce

with open("./inputs/day11.txt") as file:
    lines = [line.strip() for line in file.readlines()]

class Monkey:
    def __init__(self):
        self.id = id
        self.items = []
        self.insp_counter = 0
        self.op = ""
        self.op_factors = []
        self.test_factor = 1
        self.dest_true = -1
        self.dest_false = -1

    @staticmethod
    def create(lines):
        m = Monkey()
        m.id = int(lines[0][lines[0].find(" ") + 1:lines[0].find(":")])
        m.items = list(map(int, lines[1][lines[1].find(": ") + 2:].split(", ")))
        op = lines[2][lines[2].find("= ") + 2:]
        m.op_factors = op.split(" ")
        m.test_factor = int(lines[3].split(" ")[-1])
        m.dest_true = int(lines[4].split()[-1])
        m.dest_false = int(lines[5].split()[-1])
        return m

    def inspect_items(self, monkeys):
        for item in self.items:
            self.insp_counter += 1
            self.inspect_item(item, monkeys)
        
        self.items.clear()

    def inspect_item(self, item: int, monkeys):
        first = item if self.op_factors[0] == "old" else self.op_factors[0]
        op = self.op_factors[1]
        second = item if self.op_factors[2] == "old" else self.op_factors[2]
        new_val = eval(str(first) + op + str(second))

        if new_val % self.test_factor == 0:
            monkeys[self.dest_true].append_item(new_val)
        else:
            monkeys[self.dest_false].append_item(new_val)

    def append_item(self, item: int):
        self.items.append(item)

monkeys = []
for idx in range(0, len(lines), 7):
    monkeys.append(Monkey.create(lines[idx:idx+7]))

round_count = 20
for round in range(1, round_count + 1):
    for monkey in monkeys:
        monkey.inspect_items(monkeys)

# inspections = [monkey.insp_counter for monkey in monkeys]
# result = reduce(lambda x, y: x * y, sorted(inspections, reverse=True)[0:2])
# print(result)
for monkey in monkeys:
    print(monkey.items)