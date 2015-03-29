# DUEL variables
DUEL_DICE = 4
MAX_HP = 6

# write the action on screen
def action(roll):
    if roll == 4:
        return "blocks"
    elif roll == 3:
        return "dodges"
    elif roll == 2:
        return "swings low"
    else:
        return "swings high"

# Duel between two fighters
def duel(fighter1,fighter2):
    hp1 = MAX_HP
    hp2 = MAX_HP
    
    res = fighter1 + " and " + fighter2 + " start a duel! ("+str(MAX_HP)+"-"+str(MAX_HP)+")"
    print(res)
    while(hp1 > 0 and hp2 > 0):
        roll1 = randint(1,DUEL_DICE)
        roll2 = randint(1,DUEL_DICE)
        
        
        if roll1 == 4:
            if roll2 == 4:
                hp1 -= 0
                hp2 -= 0
            elif roll2 == 3:
                hp1 -= 0
                hp2 -= 0           
            elif roll2 == 2:
                hp1 -= 0.5
                hp2 -= 0
            else:
                hp1 -= 1
                hp2 -= 0          
        elif roll1 == 3:
            if roll2 == 4:
                hp1 -= 0
                hp2 -= 0               
            elif roll2 == 3:
                hp1 -= 0
                hp2 -= 0                
            elif roll2 == 2:
                hp1 -= 0
                hp2 -= 1                
            else:
                hp1 -= 0
                hp2 -= 0                
        elif roll1 == 2:
            if roll2 == 4:
                hp1 -= 0
                hp2 -= 0.5                
            elif roll2 == 3:
                hp1 -= 1
                hp2 -= 0                
            elif roll2 == 2:
                hp1 -= 1
                hp2 -= 1                
            else:
                hp1 -= 0.5
                hp2 -= 1           
        else:
            if roll2 == 4:
                hp1 -= 0
                hp2 -= 1                
            elif roll2 == 3:
                hp1 -= 0
                hp2 -= 0             
            elif roll2 == 2:
                hp1 -= 1
                hp2 -= 0.5             
            else:       
                hp1 -= 2
                hp2 -= 2               
        
        if hp1 < 0:
            hp1 = 0
        if hp2 < 0:
            hp2 = 0
                
        res = fighter1 + " " + action(roll1) + " and " + fighter2 +" " + action(roll2) + "! ("+str(hp1)+"-"+str(hp2)+")"
        print(res)
    if hp1 > hp2:
        print(fighter1,"has won!")
    else:
        print(fighter2,"has won!")
