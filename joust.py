# Load Joust variables
import os
from random import randint
JOUST_DICE = os.environ['DICE_JOUST']
JOUST_DEATH_ROLL_TRIGGER = os.environ['JOUST_DEATH_ROLL_DIFFERENCE']
JOUST_UNHORSE_TRIGGER = os.environ['JOUST_UNHORSE_DIFFERENCE']
JOUST_BROKEN_LANCE_TRIGGER = os.environ['JOUST_BROKEN_LANCE_DIFFERENCE']
JOUST_STRONG_HIT_TRIGGER = os.environ['JOUST_STRONG_HIT_DIFFERENCE']
JOUST_HIT_TRIGGER = os.environ['JOUST_HIT_DIFFERENCE']


# roll 2d20 taking both players' penalty into account
def tilt(malus1, malus2):
    dice1 = randint(1,JOUST_DICE) - malus1
    dice2 = randint(1,JOUST_DICE) - malus2
    dice1 = 0 if dice1 < 0 else dice1     # Dice rolls can't go under 0
    dice2 = 0 if dice2 < 0 else dice2
    return dice1,dice2



# Formats the result into something nice
def pretty_result(winner,loser,tilt_result,roll_w,roll_l):
    tilt_result = abs(tilt_result)
    if tilt_result > DEATH_ROLL_TRIGGER:
        res = loser + " is brutally unhorsed by " + winner
    elif tilt_result > UNHORSE_TRIGGER:
        res =  loser + " is unhorsed by " + winner
    elif tilt_result > BROKEN_LANCE_TRIGGER:
        res =  winner + " breaks a lance against " + loser
    elif tilt_result > STRONG_HIT_TRIGGER:
        res =  winner + " deals a strong hit to " + loser
    elif tilt_result > HIT_TRIGGER:
        res =  winner + " hits " + loser
    else:
        res = winner + " and " + loser + " exchange glancing hits"
    return res+" ["+winner+" "+str(roll_w)+", "+loser+" "+str(roll_l)+"]\n\n"


# Get the malus the loser will take
def get_malus(tilt_result):
    tilt_result = abs(tilt_result)
    if tilt_result > DEATH_ROLL_TRIGGER:
        return -1
    if tilt_result > UNHORSE_TRIGGER:
        return -1
    if tilt_result > BROKEN_LANCE_TRIGGER:
        return 3
    elif tilt_result > STRONG_HIT_TRIGGER:
        return 2
    elif tilt_result > HIT_TRIGGER:
        return 1
    else:
        return 0


def death_roll(jouster):
    roll = randint(1,JOUST_DICE)
    if roll < 5:
        return jouster + " has died! ["+str(roll)+"]\n\n"
    elif roll < 10:
        return jouster + " is maimed! ["+str(roll)+"]\n\n"
    elif roll < 15:
        return jouster + " got hurt! ["+str(roll)+"]\n\n"
    else :
        return jouster + " is fine! ["+str(roll)+"]\n\n"


# Joust to 7 tilts
def joust(rider1,rider2):
    res = "\n\n"
    malus1 = 0
    malus2 = 0
    broken_lances_1 = 0
    broken_lances_2 = 0   
    for x in range(1,8):
        rolls = tilt(malus1,malus2)
        tilt_res = rolls[0] - rolls[1]
        if tilt_res == 0:
            res += rider1 + " and " + rider2 + " miss each other ["+rider1+" "+str(rolls[0])+", "+rider2 +" "+str(rolls[1])+"]\n\n"
        else:
            if tilt_res > 0:
                winner = rider1
                loser = rider2
                roll_winner = rolls[0]
                roll_loser = rolls[1]
                malus1 += get_malus(tilt_res)
            else:
                winner = rider2
                loser = rider1
                roll_winner = rolls[1]
                roll_loser = rolls[0]
                malus2 += get_malus(tilt_res)
            res += pretty_result(winner,loser,tilt_res,roll_winner,roll_loser)
            if abs(tilt_res) > UNHORSE_TRIGGER:
               res += "DEATH ROLL: "
               res += death_roll(loser)
               res += "**"+winner+" has won!**\n\n"
               return res   
            if abs(tilt_res) > UNHORSE_TRIGGER:
               res += "**"+winner+" has won!\n\n"
               return res
            elif abs(tilt_res) > BROKEN_LANCE_TRIGGER:
                if  tilt_res > 0:
                    broken_lances_1 += 1
                else:
                    broken_lances_2 += 1
    if broken_lances_1 > broken_lances_2:
        res +="**"+rider1+" won against "+rider2+" ("+str(broken_lances_1)+" broken lances against "+str(broken_lances_2)+")**\n\n"
    elif broken_lances_1 > broken_lances_2:
        res += "**"+rider2+" won against "+rider1+" ("+str(broken_lances_2)+" broken lances against "+str(broken_lances_1)+")**\n\n"
    else:
        res += "**"+rider1+" and "+rider2+" tie with "+str(broken_lances_2)+" broken lances.**\n\n"
    return res
