#NOTE: Config file not included

import config
import praw
import os

class RedditBot:
    def __init__(self):
        print("Loggin in...")
        self.reddit = praw.Reddit(username = config.username,
                                 password = config.password,
                                 client_id = config.client_id,
                                 client_secret = config.client_secret,
                                 user_agent = "BeepBoopTestBot")

        dest = os.getcwd()+"\\"
        if not os.path.isfile(dest+'cache.txt'):
            with open("cache.txt", 'w') as f:
                self.cache_content = ""
        else:
            with open("cache.txt", 'r') as f:
                self.cache_content = f.read()

        self.run_bot()
        
    def run_bot(self):
        print("Running bot...")
        userComments = self.reddit.redditor("vargas").comments.new(limit=3)
        commentNumber = 0
        for comment in userComments:
            commentNumber += 1
            print("Comment number %d" % (commentNumber))
            print(comment.body)
            print("Score: "+str(comment.score)+'\n')
            if comment.id not in self.cache_content:
########Comment replying disabled########
##                oomment.reply("Beep Boop Hello! I am your biggest fan!")
                with open("cache.txt", 'a') as f:
                    f.write(comment.id+"\n")
        


