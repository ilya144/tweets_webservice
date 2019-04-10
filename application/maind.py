import idbclient
from iparser import TweetParser
from flask import Flask, render_template
from threading import Thread
import time

app = Flask(__name__)

class ParserThread(Thread):
    def __init__(self, parser_tweet: TweetParser):
        Thread.__init__(self)
        self.parser_tweet = parser_tweet
        self.tweets = []

    def run(self):

        while True:
            self.tweets = self.parser_tweet.get_card_tweets()
            PARSE_DELAY = 300 # задержка между парсиногом твитов
            time.sleep(PARSE_DELAY)




@app.route("/")
def respone():
    #return "Hello World!"
    return render_template('index.html', tweets = parser_thread.tweets)


if __name__ == "__main__":
    with open("../followed.txt") as f:
        string = f.read()
        accounts = string.split("\n")
    parser_tweet = TweetParser(accounts)
    parser_thread = ParserThread(parser_tweet)
    parser_thread.start()
    HOST = 'localhost'
    PORT = '5000'
    app.run(host= HOST, port= PORT)