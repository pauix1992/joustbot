# Melee variables
from random import randint
MELEE_DICE = 50



# Takes a melee comment and runs the melee.
def melee(comment):
    body = comment.body
    b = body.split("\n")
    contestants = []
    for contestant in b:
        # Checks if there's a contestant to add.
        if contestant.find("joustbot") < 0 and len(contestant) > 4:
            survivors.append(contestant[2:-2])
    i = 1
    while(len(survivors) > 1:
        res = "### ROUND " + str(i) + "\n\n"
        r_min = 200
        roll = [None]*len(survivors)
        a = []
        for i in range(0,len(survivors)):
            # everyone rolls
            player = survivors[i].split(',')
            
            roll[i] = randint(1,50)
            if len(player) > 1:
                roll[i] = roll[i]+int(player[1])
                clean = int(roll[i])-int(player[1])
            if roll[i] < r_min:
                r_min = roll[i]
            res += player[0] + " rolls a " + str(roll[i])
            if len(player) > 1:
                res+=" (" + str(clean) + " + " + str(player[1])+ ")"
            res += "\n\n"
        for i in range(0,len(roll)):
            if roll[i] == r_min:
                player = survivors[i].split(',')
                res += "**"+player[0] + " has been eliminated!**\n\n"
            else:
                a.append(survivors[i])

        survivors = a
        comment = comment.reply(res)
        sleep(2)
        ++i

    if len(survivors) == 1:
        player = survivors[0].split(',')
        res = res + player[0] + " has won!"

    else:
        return "ERROR: Last round should be re-rolled!"

