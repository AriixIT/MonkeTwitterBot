import tweepy
import time
import os, random

print('This is my bot mf')

CONSUMER_KEY = 'mNX6sVBHwcjqtviePqOGq6j5U'
CONSUMER_SECRET = 'MAnGO1fAlftT19rcBx3FbeBc8dtq8p4HEW8fGV6Ra6PftyhOpo'
ACCESS_KEY = '1364127981787095041-2X0WrlL3B3x3PPHmmdSr4ZU8bwgaTM'
ACCESS_SECRET = 'btPB1TQFaDgM1N9Y9dfeO82mFY83cscr4584ZRl26F7LM'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

DIRECTORY = "D:\\programming\\Github\\MonkeTwitterBot\\pictures\\"
FILE_NAME = 'last_seen_id.txt'


def retrieve_last_seen_id():
    f_read = open(FILE_NAME, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def store_last_seen_id(last_seen_id):
    f_write = open(FILE_NAME, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def reply_to_tweets():
    #quoteFile = open("testFile.txt")
    # api.update_status(quoteFile.read())
    last_seen_id = retrieve_last_seen_id()
    mentions = api.mentions_timeline(since_id = last_seen_id)
    for mention in reversed(mentions):
        if "Monke" in mention.text:
            print('replying to ' + str(mention.id))
            try:
                filename = random.choice([x for x in os.listdir(DIRECTORY) if os.path.isfile(os.path.join(DIRECTORY, x))])
                response = api.media_upload(DIRECTORY + filename)
                if api.update_status("Monke", media_ids = [response.media_id], in_reply_to_status_id = mention.id, auto_populate_reply_metadata=True):
                    last_seen_id = mention.id
                    store_last_seen_id(last_seen_id)
            except tweepy.errors.TweepyException:
                print("fuck")


while(True):
    reply_to_tweets()
    time.sleep(15)