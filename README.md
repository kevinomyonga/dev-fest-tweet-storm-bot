# Dev-Fest-Tweet-Storm-Bot

GDG Nairobi Dev Fest Twitter Post Competition Hack Bot.

This project was developed by [Kevin Omyonga](https://kevinomyonga.com).

## Built With

- [Python](https://www.python.org) - Programming Language

## How To Run It?

Create a virtual environment:

    python -m venv .venv

Install the requirements from the requirements.txt file:

    pip install -r requirements.txt

Create a .env file and add the required credential from the [Twitter Developer Portal](https://developer.twitter.com).

    CONSUMER_KEY="CONSUMER_KEY"
    CONSUMER_SECRET="CONSUMER_SECRET"
    ACCESS_TOKEN="ACCESS_TOKEN"
    ACCESS_TOKEN_SECRET="ACCESS_TOKEN_SECRET"

Add the tweets you wish to post in the tweets_pending.txt file

Run the script to post tweets:

    python rainfire/post_tweet.py

## Contribute

Got any ideas on how to make this better? Feedback and pull requests are welcome.

## Contact

Want to get in touch?

You can follow me on

Twitter: [@kevinomyonga](https://twitter.com/kevinomyonga).

LinkedIn: [Kevin Omyonga](https://twitter.com/kevinomyonga).
