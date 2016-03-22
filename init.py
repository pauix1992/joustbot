# load reddit suite
import os
import praw
from time import sleep;
from random import randint;


# import custom classes
from joust import *
from melee import *
from archery import *
from horse_racing import *
from duel import *

# Array that stores the IDs of checked comments
checked_comments = []

# Run the bot
def start_bot():
    r = praw.Reddit(user_agent = 'IronThronePowers thingy')
    r.login('joustbot','BlackGoatOfQohor')
    subreddits = r.get_subreddit('qohorpowers+ironthronepowers') # Currently ITP, WP and some test subreddits.
    comments = subreddits.get_comments(limit=100)
    comments = subreddits.get_comments()    

    # Load all parsed comments to prevent joustbot from answering to them again.
    for comment in comments:
        checked_comments.append(comment.id)
    print("READY TO ROCK!")
    # Keep searching for comments.
    while(1):
        find_new_comments(subreddits)
        sleep(60)



# Function the bot will use to find new comments
def find_new_comments(subreddits):
    comments = subreddits.get_comments(limit=100)    
    for comment in comments:
        body = comment.body
        if comment.id not in checked_comments:
           
            if body.find("joustbot joust") >= 0:
                print("rolling a joust")
                b = body.split("\n")
                result = ''
                for pair in b:
                   c = pair.split(" - ")
                   if len(c) > 1:
                       d = c[0]
                       d = d.split(",")
                       e = c[1]
                       e = e.split(",")
		       if len(d) > 1:
                           b1 = d[1]
                       else:
                           b1 = 0
                       if len(e) > 1:
                           b2 = e[1]
                       else:
                           b2 = 0

                       result +="***" + d[0] + " VERSUS " + e[0] + "!***\n\n"
                       result += joust(d[0],e[0],b1,b2) or "ERROR!"
                       result += "------------------------------------------------------\n\n"
                comment.reply(result[:9999])
                if len(result) > 10000:
                   comment.reply(result[10000:19999])
                if len(result) > 20000:
                   comment.reply(result[20000:29999])
       
       
            elif body.find("joustbot melee") >= 0:
                print("rolling a melee")
                melee(comment)
       
       
            elif body.find("joustbot horse race") >= 0:
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
       
       
            elif body.find("joustbot archery") >= 0:
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

            elif body.find("joustbot patrol") >= 0:
                print("roll for a patrol. NO DONE YET")
#                b = body.split("\n")
#                c = []
#                for contestant in b:
#                    if contestant.find("joustbot") < 0:
#                        c.append(contestant)
#                result = archery(*c)
#                comment.reply(result[:9999])
#                if len(result) > 10000:
#                    comment.reply(result[10000:19999])
#                if len(result) > 20000:
#                    comment.reply(result[20000:29999])


            elif body.find("joustbot duel") >= 0:
                print("rolling a duel")
                b = body.split("\n")
                result = ''
                for pair in b:
                    c = pair.split(" - ")
                    if len(c) > 1:
                        result +="***" + c[0] + " VERSUS " + c[1] + "!***\n\n"
                        result += duel(c[0],c[1]) or "ERROR!"
                        result += "------------------------------------------------------\n\n"
                comment.reply(result[:9999])
                if len(result) > 10000:
                    comment.reply(result[10000:19999])
                if len(result) > 20000:
                    comment.reply(result[20000:29999])
 
            checked_comments.append(comment.id)
