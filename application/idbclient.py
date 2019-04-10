#	http://api.mongodb.com/python/current/tutorial.html
import pymongo


class Database:
    """
    class for connection and  work with MongoDB
    ALL tweets looks like
    {
    'from' : string, # username
    'url' : string # tweet url
    }
    """

    def __init__(self) -> None:
        self.client = pymongo.MongoClient()
        self.db = self.client.tweet_db
        self.tweets = self.db.tweets
        self.tweets.create_index([('url', pymongo.ASCENDING)], unique=True)


    def add_tweet(self, tweet: dict) -> None:# add new tweent into db
        try:
            self.tweets.insert_one(tweet)
        except Exception as e:
            return "Error: %s"%str(e)

    def add_tweets(self, tweets: list) -> None: # add new tweents into db
        try:
            self.tweets.insert_many(tweets)
        except Exception as e:
            return "Error: %s"%str(e)

    def get_tweet_by_name(self, name) -> dict:# find tweets by username
        return self.tweets.find_one({'from':name})

    def get_tweet_by_url(self, url) -> dict: # find tweet by url
        return self.tweets.find_one({'url':url})

    def get_last_url(self, count):# get last 10 tweet urls
        tweets = []
        for tweet in self.tweets.find():
            tweets.append(tweet['url'])
        return tweets[-1:-1-count:-1]