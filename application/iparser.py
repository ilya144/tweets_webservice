from bs4 import BeautifulSoup
import requests

class TweetParser:

    def __init__(self, accs):
        self.accs = accs


    def parse_tweets(self) -> list: # получаю список json'a твитов с фото/видео
        all_tweets = []
        for acc in self.accs:
            r = requests.get("https://twitter.com/%s" % acc)
            #print(r.status_code)
            soup = BeautifulSoup(r.content, 'html.parser')
            list_tweets = soup.find(id="timeline").find('ol').find_all(class_='js-stream-item')
            #print(len(list_tweets))
            for tweet in list_tweets:
                if 'data-has-cards' in list(tweet.children)[1].attrs:

                    tweet_username = list(tweet.children)[1].attrs['data-screen-name'] # load username
                    tweet_url = list(tweet.children)[1].attrs['data-permalink-path'] # load url
                    tweet_dict = {'from': tweet_username, 'url': tweet_url}

                    all_tweets.append(tweet_dict)

        return all_tweets


if __name__ == "__main__": # parse sandbox
    with open("../followed.txt") as f:
        string = f.read()
        accounts = string.split("\n")
        print(accounts)
    r = requests.get("https://twitter.com/%s"%accounts[2])
    print(r.status_code)
    soup = BeautifulSoup(r.content, 'html.parser')
    list_tweets = soup.find(id="timeline").find('ol').find_all(class_='js-stream-item')
    print(len(list_tweets))
    for tweet in list_tweets:
        if 'data-has-cards' in list(tweet.children)[1].attrs:
            print(list(tweet.children)[1].attrs)
