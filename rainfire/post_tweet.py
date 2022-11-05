#!/usr/bin/env python

"""
This file is part of Tweet Storm Bot.

Copyright (c) 2022 - Kevin Omyonga
"""

import logging
import os
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# list to store file tweets
tweet_list = []

# Pending file
pending_file = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "tweets_pending.txt"
)

# Posted file
posted_file = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "tweets_posted.txt"
)

# read file
with open(pending_file, "rt") as fp:
    # read an store all lines into list
    tweet_list = fp.readlines()

dev_fest_hashtags = "#DevFest2022 #DevFestNairobi #CodeToInfinityAndBeyond"


def post_tweet(api):
    logger.info("Posting Tweet")
    for x in range(len(tweet_list)):
        # Print selected tweet
        print(f"{tweet_list[x]} {dev_fest_hashtags}")

        # Create a tweet
        api.update_status(f"{tweet_list[x]} {dev_fest_hashtags}")

        # Write to posted file
        with open(posted_file, "a") as fp:
            fp.write(tweet_list[x])


def main():
    api = create_api()
    while True:
        post_tweet(api)
        logger.info("Done Posting...")
        time.sleep(60)


if __name__ == "__main__":
    main()
