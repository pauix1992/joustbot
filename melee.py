# Melee variables

MELEE_DICE = os.environ['DICE_MELEE']



## Run a melee fight until no more than 2 contestants are left.
# arg is a list of contestants
# If 2 contestants remain, the final duel must be still run manually 
# If 1 player remains, he's considered the winner.

def melee(comment,*arg):
    res=''
    survivors = list(arg)
    while len(survivors) > 2:
        r_min = MELEE_DICE+1
        roll = [None]*len(survivors)
        a = []
        for i in range(0,len(survivors)):
            # everyone rolls
            roll[i] = randint(1,MELEE_DICE)
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
        sleep(10)
    if len(survivors) == 1:
        return res + survivors[0] + " has won!"
    elif len(survivors) == 2:
        return res + survivors[0] + " and " + survivors[1] + " will have the final duel!"
    


 



