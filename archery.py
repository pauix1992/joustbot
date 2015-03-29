# Archery variables
ARCHERY_DICE = 100 # os.environ['DICE_ARCHERY']


## Run an archery competition. 
# *arg is a list with all the contestants

def archery(*arg):
    bullseye = randint(1,ARCHERY_DICE)
    res='**BULLSEYE IS '+str(bullseye)+'**\n\n'
    score = [0]*len(arg)
    for i in range(0,len(arg)-1):
        score[i] = 0
    for i in range(1,4):
        rolls = [None]*len(arg)
        res += "**ROUND "+str(i)+"**\n\n"
        for j in range(0,len(arg)-1):
            rolls[j]  = randint(1,ARCHERY_DICE)
            c_score = int(rolls[j]-bullseye)
            score[j] += abs(c_score)
            res += arg[j] + " rolls a " + str(rolls[j])
            if rolls[j] == bullseye:
                res += "(bullseye)"
            res += "\n\n"
        res += "----------\n\n"
    min_score = 3*ARCHERY_DICE
    for j in range(0,len(arg)-1):
        if score[j] < min_score:
            min_score = score[j]
    winners = [] 
    for j in range(0,len(arg)-1):
        if score[j] == min_score:
            winners.append(arg[j])
    res += "WINNERS: \n\n"
    for contestant in winners:
        res += "* " +contestant+"\n\n"
    return res
