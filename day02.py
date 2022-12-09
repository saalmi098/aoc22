scores = {
    "A": 1,
    "B": 2,
    "C": 3,
}

with open('./inputs/day02.txt') as file:
    lines = [line.rstrip() for line in file]

def get_result1(myTurn, opponentTurn):
    win, draw = 6, 3
    myTurn = myTurn.replace("X", "A").replace("Y", "B").replace("Z", "C")
    score = scores[myTurn]

    if myTurn == opponentTurn:
        return draw + score # draw

    won = (myTurn == "A" and opponentTurn == "C") or (myTurn == "B" and opponentTurn == "A") or (myTurn == "C" and opponentTurn == "B")
    if won:
        return win + score

    return score

def get_result2(result, opponentTurn):
    win, draw = 6, 3
    score = 0

    if result == "Y":
        # draw
        score += draw
        myTurn = opponentTurn
    elif result == "X":
        # lose
        if opponentTurn == "A": myTurn = "C"
        elif opponentTurn == "B": myTurn = "A"
        elif opponentTurn == "C": myTurn = "B"
    elif result == "Z":
        # win
        score += win
        if opponentTurn == "A": myTurn = "B"
        elif opponentTurn == "B": myTurn = "C"
        elif opponentTurn == "C": myTurn = "A"

    score += scores[myTurn]
    return score

score = 0
for line in lines:
    opponentTurn, myTurn = line.split(' ')
    #score += get_result1(myTurn, opponentTurn)
    score += get_result2(myTurn, opponentTurn)

print(score)
