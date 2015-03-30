# Horse racing variables
from random import randint
HORSE_RACING_DICE = 20
HORSE_RACING_DEATH_ROLL_TRIGGER = 10
HORSE_RACING_DEATH_TRIGGER = 3
HORSE_RACING_HANDICAP_TRIGGER = 6
HORSE_RACING_SCAR_TRIGGER = 10

## Roll a death roll for someone
def horse_racing_death_roll():
    roll = randint(1,HORSE_RACING_DICE)
    if roll < HORSE_RACING_DEATH_TRIGGER:
        return " has died! ("+str(roll)+")"
    elif roll < HORSE_RACING_HANDICAP_TRIGGER:
        return " is now handicapped! ("+str(roll)+")"
    elif roll < HORSE_RACING_SCAR_TRIGGER:
        return " will have a scar for life! ("+str(roll)+")"
    elif roll < HORSE_RACING_DEATH_ROLL_TRIGGER:
        return " has been wounded! ("+str(roll)+")"
    else:
        return " is fine! ("+str(roll)+")"

## Rolls a dice for a contestant. 
# If the contestant is not dornish, he gets a -2
def horse_racing_roll(contestant):
    c = contestant.split(" - ")
    if c[1].find("Dorne") >= 0:
        return randint(1,HORSE_RACING_DICE)
    else:
        return randint(-1,HORSE_RACING_DICE-2)

## Run a horse race until one man remains.
# *arg is a list of contestants
def horse_racing(*arg):
    res=''
    survivors = list(arg)
    while len(survivors) > 1:
        r_min = HORSE_RACING_DICE+1
        roll = [None]*len(survivors)
        a = []
        for i in range(0,len(survivors)):
            c = survivors[i].split(" - ")
            # everyone rolls
            roll[i] = horse_racing_roll(arg[i])
            if roll[i] < r_min:
                r_min = roll[i]
            res += c[0] + " rolls a " + str(roll[i])+"\n\n"
        for i in range(0,len(roll)):
            c = survivors[i].split(" - ")
            if roll[i] == r_min:
                if roll[i] < HORSE_RACING_DEATH_ROLL_TRIGGER:
                    res += "**"+c[0] + " has been eliminated and"
                    res += horse_racing_death_roll()+"**\n\n"
                else:
                    res += "**"+c[0] + " has been eliminated!**\n\n"
            else:
                a.append(survivors[i])
        survivors = a
        res += "-------------------------------------\n\n"
    if len(survivors) == 1:
        c = survivors[0].split(" - ")
        return res + c[0] + " has won!"

