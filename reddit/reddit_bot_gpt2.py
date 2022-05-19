import praw
import config
import time
import os
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# set stuffs as pre-trained models
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# login to the Reddit bot
def login():
    print("Logging in")

    # logging in
    reddit = praw.Reddit(username = config.USERNAME, password = config.PASSWORD, 
                    client_id = config.CLIENT_ID, client_secret = config.CLIENT_SECRET,
                    user_agent = "notburningthebible ai bot v0.1.0")

    print("Logged in")

    return reddit # returning the login

# run the Reddit bot
def run(reddit):
    global misinformation_example_found 
    misinformation_example_found = ""

    for comment in reddit.subreddit("test").comments(limit=10): # check the subreddit within 10 comments
        misinformation_examples = ["flat earth", "anti-mask", "anti-vax"]

        for i in range(len(misinformation_examples)):
            if misinformation_examples[i] in comment.body and comment.id not in comment_ids and comment.author != reddit.user.me():
                print(str(misinformation_examples[i]) + " detected at " + comment.id)
                misinformation_example_found = misinformation_examples[i]

        if misinformation_example_found in comment.body and comment.id not in comment_ids and comment.author != reddit.user.me(): # 'comment' is the loop item /// check for the specified word // check if the comment has already been replied to // make sure the author is not the bot
            #print("\"Fahrenheit\" detected at " + comment.id) # print "[] detected" if [] found

            sequence = (comment.body) # uses the comment as the base for the response
            input = tokenizer.encode(sequence, return_tensors='pt') # tokenise the sequence
            output = model.generate(input, max_length=200, do_sample=True) # generate the model with max length 200
            text = tokenizer.decode(output[0], skip_special_tokens=True) # decode the stuffs
            comment.reply(text) # send a reply
            print("Replied to " + comment.id) # confirm reply

            comment_ids.append(comment.id) # add comment id to commend_ids list
            print(comment_ids) # print comment_ids list

            #with open("comments_replied.txt", "a") as f: # open the file
            #    f.write(comment.id + "\n") # write the new comment's id

            print("Sleeping...") # print that it is sleeping
            time.sleep(2) # sleep for 2 seconds

    print("Sleeping...") # print that it is sleeping
    time.sleep(10) # sleep for 10 seconds

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