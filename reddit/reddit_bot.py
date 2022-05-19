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
                    user_agent = "notburningthebible bot v0.2.1")

    print("Logged in")

    return reddit # returning the login

# run the Reddit bot
def run(reddit):
    for comment in reddit.subreddit("test").comments(limit=10): # check the subreddit within 10 comments
        if "flat" and "earth" in comment.body and comment.id not in comment_ids and comment.author != reddit.user.me():
            print("\"flat\" and \"earth\" detected at " + comment.id) # print "[] detected if books found"

            comment.reply("The Earth is not flat. Everyone should know by now that it is a dinosaur") # send a reply
            print("Replied to " + comment.id) # confirm reply

            comment_ids.append(comment.id) # add comment id to commend_ids list
            print(comment_ids) # print comment_ids list

            print("Writing to text file...")
            with open("comments_replied.txt", "a") as f: # open the file
                f.write(comment.id + "\n") # write the new comment's id
            print("Added comment ID to text file")

        if "anti-vax" in comment.body and comment.id not in comment_ids and comment.author != reddit.user.me():
            print("\"anti-vax\" detected at " + comment.id) # print "[] detected if books found"

            comment.reply("Being against vaccines is deadly. [Get vaccinated](https://www.vaccines.gov/).") # send a reply
            print("Replied to " + comment.id) # confirm reply

            comment_ids.append(comment.id) # add comment id to commend_ids list
            print(comment_ids) # print comment_ids list

            print("Writing to text file...")
            with open("comments_replied.txt", "a") as f: # open the file
                f.write(comment.id + "\n") # write the new comment's id
            print("Added comment ID to text file")

        if "anti-mask" in comment.body and comment.id not in comment_ids and comment.author != reddit.user.me():
            print("\"anti-mask\" detected at " + comment.id) # print "[] detected if books found"

            comment.reply("Being against masks is dangerous. [Put one on](https://www.cdc.gov/coronavirus/2019-ncov/your-health/free-masks.html).") # send a reply
            print("Replied to " + comment.id) # confirm reply

            comment_ids.append(comment.id) # add comment id to commend_ids list
            print(comment_ids) # print comment_ids list

            print("Writing to text file...")
            with open("comments_replied.txt", "a") as f: # open the file
                f.write(comment.id + "\n") # write the new comment's id
            print("Added comment ID to text file")
        
        """if "flat" and "earth" in comment.body and comment.id not in comment_ids and comment.author != reddit.user.me: # 'comment' is the loop item /// check for a specified word // check if the comment has already been replied to // make sure the author is not the bot
            replying_to_comment(comment, 0)
        elif "anti-vax" in comment.body and comment.id not in comment_ids and comment.author != reddit.user.me: # 'comment' is the loop item /// check for a specified word // check if the comment has already been replied to // make sure the author is not the bot
            replying_to_comment(comment, 1)
        elif "anti-mask" in comment.body and comment.id not in comment_ids and comment.author != reddit.user.me: # 'comment' is the loop item /// check for a specified word // check if the comment has already been replied to // make sure the author is not the bot
            replying_to_comment(comment, 2)"""
            
        """print("\"flat\" and \"earth\" detected at " + comment.id) # print "[] detected if books found"

            comment.reply("The Earth is not flat") # send a reply
            print("Replied to " + comment.id) # confirm reply

            comment_ids.append(comment.id) # add comment id to commend_ids list
            print(comment_ids) # print comment_ids list"""

        """print("Writing to text file...")
        with open("comments_replied.txt", "a") as f: # open the file
            f.write(comment.id + "\n") # write the new comment's id
        print("Added comment ID to text file")"""
    
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

# replying function
def replying_to_comment(comment_id, complaint_id):
    complaint_response = ["The Earth is not flat. Everyone should know by now that it is a dinosaur", "Being against vaccines is deadly. [Get vaccinated](https://www.vaccines.gov/).", "Being against masks is dangerous. [Put one on](https://www.cdc.gov/coronavirus/2019-ncov/your-health/free-masks.html)."]
    
    print("Complaint " + str(complaint_id) + " detected at " + comment_id.id) # print "[] detected if books found"

    comment_id.reply(complaint_response[complaint_id]) # send a reply
    print("Replied to " + comment_id.id) # confirm reply

    if comment_id in comment_ids:
        pass
    else:
        comment_ids.append(comment_id.id) # add comment id to commend_ids list
        print(comment_ids) # print comment_ids list

    print("Sleeping for 15s...") # print that it is sleeping
    time.sleep(15) # sleep for 15 seconds

"""
Hello
"""

# creates a list of comment ids
comment_ids = comments_replied() 

# running the bot
while True:
    reddit = login() # logging in

    run(reddit) # run the bot