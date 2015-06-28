# Melee variables
from random import randint
MELEE_DICE = 50


## Run a melee fight until no more than 2 contestants are left.
# arg is a list of contestants
# If 2 contestants remain, the final duel must be still run manually 
# If 1 player remains, he's considered the winner.

def melee(comment):
    b = comment.body
    b = body.split("\n")
    contestants = []
    for contestant in b:
        if contestant.find("joustbot") < 0:
            c.append(contestant[3:-3])

    result = melee_recursive(*c)


    comment.reply(result[:9999])
    if len(result) > 10000:
        comment.reply(result[10000:19999])
    if len(result) > 20000:
        comment.reply(result[20000:29999])             
    print(result)


def melee_recursive(*arg):
    res=''
    survivors = list(arg)
    while len(survivors) > 2:
        r_min = 2*MELEE_DICE
        roll = [None]*len(survivors)
        a = []
        for i in range(0,len(survivors)):
            # everyone rolls
            bonus = survivors[i].split(',')
            roll[i] = randint(1,MELEE_DICE)+int(bonus)
            if roll[i] < r_min:
                r_min = roll[i]
            res += survivors[i] + " rolls a " + str(roll[i])+"\n\n"
        for i in range(0,len(roll)):
            if roll[i] == r_min:
                res += "**"+survivors[i] + " has been eliminated!**\n\n"
            else:
                a.append(survivors[i])
        survivors = a
        res += "-------------------------------------\n\n"
    if len(survivors) == 1:
        return res + survivors[0] + " has won!"
    elif len(survivors) == 2:
        return res + survivors[0] + " and " + survivors[1] + " will have the final duel!"
    


 



