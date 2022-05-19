import praw
import config
import time
import os

# login to the Reddit bot
def login():
    print("Logging in")

    # logging in
    reddit = praw.Reddit(username = config.USERNAME, password = config.PASSWORD, 
                    client_id = config.CLIENT_ID, client_secret = config.CLIENT_SECRET,
                    user_agent = "notburningthebible bot v0.1.2")

    print("Logged in")

    return reddit # returning the login

# run the Reddit bot
def run(reddit):
    for comment in reddit.subreddit("test").comments(limit=10): # check the subreddit within 10 comments     ##### vvvvv This does not work vvvvv #####
        if "flat" and "earth" or "anti-vax" or "anti-mask" in comment.body and comment.id not in comment_ids and str(comment.author) != "notburningthebible": # 'comment' is the loop item /// check for the word "books" // check if the comment has already been replied to // make sure the author is not the bot
            if comment.author != "notburningthebible":
                print("Misinformation detected at " + comment.id) # print "Books detected if books found"
                
                comment.reply("It appears that you have posted misinformation about the shape of the Earth, vaccines, or masks. \n \n \n Regarding the shape of the Earth, everyone should know that it is modelled after a dinosaur. \n \n Regarding vaccines, they [work](https://www.cdc.gov/coronavirus/2019-ncov/vaccines/effectiveness/work.html). [Get vaccinated](https://www.vaccines.gov/) please, for everyone's safety. \n \n Regarding masks, they are safe and work. Please [wear one](https://www.cdc.gov/coronavirus/2019-ncov/your-health/free-masks.html).") # send a reply
                print("Replied to " + comment.id + " from " + str(comment.author)) # confirm reply

                comment_ids.append(comment.id) # add comment id to commend_ids list
                print(comment_ids) # print comment_ids list

                with open("comments_replied.txt", "a") as f: # open the file
                    f.write(comment.id + "\n") # write the new comment's id

            print("Sleeping for 15s...") # print that it is sleeping
            time.sleep(15) # sleep for 15 seconds
    
    print("Sleeping for 30s...") # print that it is sleeping
    time.sleep(30) # sleep for 30 seconds

# save comments into a text file
def comments_replied():
    if not os.path.isfile("comments_replied.txt"): # looking for the file
        comments_replied = []
    else:
        with open("comments_replied.txt", "r") as f: # opening file
            comments_replied = f.read() # reading file
            comments_replied = comments_replied.split("\n") # line breaking file
    
    return comments_replied # returning the file's list

"""
Hello
"""

# creates a list of comment ids
comment_ids = comments_replied() 


# running the bot
while True:
    reddit = login() # logging in

    run(reddit) # run the bot