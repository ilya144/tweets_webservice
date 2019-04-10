from bs4 import BeautifulSoup
import requests

class TweetParser:

    def __init__(self, accs):
        self.accs = accs

    def get_card_tweets(self) -> list: # получаю твиты только с фото/видео контентом
        all_tweets_urls = []
        for acc in self.accs:
            r = requests.get("https://twitter.com/%s" % acc)
            #print(r.status_code)
            soup = BeautifulSoup(r.content, 'html.parser')
            list_tweets = soup.find(id="timeline").find('ol').find_all(class_='js-stream-item')
            #print(len(list_tweets))
            for tweet in list_tweets:
                if 'data-has-cards' in list(tweet.children)[1].attrs:
                    all_tweets_urls.append(list(tweet.children)[1].attrs['data-permalink-path'])
        return all_tweets_urls


if __name__ == "__main__":
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


# 'data-tweet-nonce': '1103657493786435584-8b95820a-f3fd-4fd6-87cf-4bd052cf97f3' where 1103657493786435584 is
# part of url https://twitter.com/golubev_vu/status/1103657493786435584  _easy
# more ease that thing 'data-permalink-path'
# e.g. https://twitter.com + list(tweet.children)[1].attrs['data-permalink-path'] == useful url