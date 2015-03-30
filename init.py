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
    r = praw.Reddit('/u/pauix bot for running jousts and melees')
    r.login('joustbot','BlackGoatOfQohor')
    subreddits = r.get_subreddit('qohorpowers+ironthronepowers+stannispowers+woiafpowers')
    comments = subreddits.get_comments(limit=100)
    comments = subreddits.get_comments()    
    for comment in comments:
        checked_comments.append(comment.id)

    while(1):
        try:
            find_new_comments(subreddits)
        except Exception:
        print("SOMETHING FUCKED UP!")
        sleep(60)



# Function the bot will use to find new comments
def find_new_comments(subreddits):
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
       
       
            elif body.find(" melee") >= 0:
                print("rolling a melee")
               b = body.split("\n")
               c = []
               for contestant in b:
                   if contestant.find("joustbot") < 0:
                       c.append(contestant)
               result = melee(*c)
               comment.reply(result[:9999])
               if len(result) > 10000:
                   comment.reply(result[10000:19999])
               if len(result) > 20000:
                   comment.reply(result[20000:29999])             
                   print(result)
       
       
            elif body.find(" horse race") >= 0:
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
       
       
            elif body.find(" archery") >= 0:
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
