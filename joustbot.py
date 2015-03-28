# load reddit suite
import praw
from time import sleep;
from random import randint;


# constants

DEATH_ROLL_TRIGGER = 17
UNHORSE_TRIGGER = 15
BROKEN_LANCE_TRIGGER = 10
STRONG_HIT_TRIGGER = 7
HIT_TRIGGER = 3

MELEE_DICE = 50
JOUST_DICE = 20

HORSE_RACING_DICE = 20
HORSE_RACING_DEATH_ROLL_TRIGGER = 10
HORSE_RACING_DEATH_TRIGGER = 3
HORSE_RACING_HANDICAP_TRIGGER = 6
HORSE_RACING_SCAR_TRIGGER = 7

ARCHERY_DICE = 100



# ARCHERY

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

def horse_racing_roll(contestant):
    c = contestant.split(" - ")
    if c[1].find("Dorne") >= 0:
        return randint(1,HORSE_RACING_DICE)
    else:
        return randint(-1,HORSE_RACING_DICE-2)


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
        sleep(10)
    if len(survivors) == 1:
        c = survivors[0].split(" - ")
        return res + c[0] + " has won!"











# MELEE FIGHT

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

checked_comments = []

r = praw.Reddit('/u/pauix bot for running jousts and melees')
r.login('joustbot','BlackGoatOfQohor')
subreddits = r.get_subreddit('qohorpowers+ironthronepowers+stannispowers+woiafpowers')
comments = subreddits.get_comments(limit=100)


def find_new_comments():
    comments = subreddits.get_comments()    
    for comment in comments:
        body = comment.body
        if body.find("joustbot") >= 0 and comment.id not in checked_comments:
            if body.find(" joust") >= 0:
                print("rolling a joust")
                b = body.split("\n")
                result = ''
                for pair in b:
                    c = pair.split(" - ")
                    if len(c) > 1:
                        result +="***" + c[0] + " VERSUS " + c[1] + "!***\n\n"
                        result += joust(c[0],c[1]) or "ERROR!"
                        result += "------------------------------------------------------\n\n"
                comment.reply(result[:9999])
                if len(result) > 10000:
                    comment.reply(result[10000:19999])
                if len(result) > 20000:
                    comment.reply(result[20000:29999])
            elif body.find("melee") >= 0:
                print("rolling a melee")
                b = body.split("\n")
                c = []
                for contestant in b:
                    if contestant.find("joustbot") < 0:
                        c.append(contestant)
                result = melee(*c)
                comment.reply(result[:9999])
                if len(result) > 10000:
                    print("rolling a horse race")
                    comment.reply(result[10000:19999])
                if len(result) > 20000:
                    comment.reply(result[20000:29999])             
                    print(result)
            elif body.find("horse race") >= 0:
                print("rolling a horse race")
                b = body.split("\n")
                c = []
                for contestant in b:
                    if contestant.find("joustbot") < 0:
                        c.append(contestant)
                result = horse_racing(*c)
                comment.reply(result[:9999])
                if len(result) > 10000:
                    comment.reply(result[10000:19999])
                if len(result) > 20000:
                    comment.reply(result[20000:29999])
            elif body.find("archery") >= 0:
                print("rolling an archery competition")
                b = body.split("\n")
                c = []
                for contestant in b:
                    if contestant.find("joustbot") < 0:
                        c.append(contestant)
                result = archery(*c)
                comment.reply(result[:9999])
                if len(result) > 10000:
                    comment.reply(result[10000:19999])
                if len(result) > 20000:
                    comment.reply(result[20000:29999])
            checked_comments.append(comment.id)


comments = subreddits.get_comments()    
for comment in comments:
    checked_comments.append(comment.id)

while(1):
    try:
        find_new_comments()
    except Exception:
        print("SOMETHING FUCKED UP!")
    sleep(60)
