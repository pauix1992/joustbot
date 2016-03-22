# Archery variables
from random import randint
ARCHERY_DICE =  100


## Run an archery competition. 
# *contestants is a list with all the contestants

def archery(comment):
    body = comment.body
    b = body.split("\n")
    contestants = []
    for contestant in b:
        # Checks if there's a contestant to add.
        if contestant.find("joustbot") < 0 and len(contestant) > 4:
            contestants.append(contestant[2:-2])







    bullseye = randint(1,ARCHERY_DICE)
    res='**BULLSEYE IS '+str(bullseye)+'**\n\n'
    score = [0]*len(contestants)
    for i in range(0,len(contestants)-1):
        score[i] = 0
    for i in range(1,4):
        rolls = [None]*len(contestants)
        res += "**ROUND "+str(i)+"**\n\n"
        for j in range(0,len(contestants)-1):
            rolls[j]  = randint(1,ARCHERY_DICE)
            c_score = int(rolls[j]-bullseye)
            score[j] += abs(c_score)
            res += contestants[j] + " rolls a " + str(rolls[j]) + "(" + str(abs(c_score)) + " away)"
            if rolls[j] == bullseye:
                res += "(bullseye)"
            res += "\n\n"
        res += "----------\n\n"
    min_score = 3*ARCHERY_DICE
    for j in range(0,len(contestants)-1):
        if score[j] < min_score:
            min_score = score[j]
    winners = [] 
    for j in range(0,len(contestants)-1):
        if score[j] == min_score:
            winners.append(contestants[j])
    res += "WINNERS: \n\n"
    for contestant in winners:
        res += "* " +contestant+"\n\n"
    print(res)
