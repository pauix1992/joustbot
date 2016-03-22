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
            contestants.append(contestant[2:-2])

    result = melee_recursive(comment,1,*contestants)

    # print result
    comment.reply(result[:9999])
    if len(result) > 10000:
        comment.reply(result[10000:19999])
    if len(result) > 20000:
        comment.reply(result[20000:29999])             
    print(result)


## Run a melee fight until no more than 2 contestants are left.
# arg is a list of contestants
# If 2 contestants remain, the final duel must be still run manually 
# If 1 player remains, he's considered the winner.
def melee_recursive(comment,ronda,*arg):
    res="# ROUND "+str(ronda)+"\n\n"
    survivors = list(arg)
    if len(survivors) > 2:
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
        comment.reply(res);
        return melee_recursive(comment,ronda+1,*survivors);


    if len(survivors) == 1:
        player = survivors[0].split(',')
        return res + player[0] + " has won!"
    elif len(survivors) == 2:
        player1 = survivors[0].split(',')
        player2 = survivors[1].split(',')
        return res + player1[0] + " and " + player2[0] + " will have the final duel!"
    



