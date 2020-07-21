from bs4 import BeautifulSoup
import requests

Source = requests.get('https://ethans_fake_twitter_site.surge.sh/').text

Tweet = BeautifulSoup(Source, 'html.parser')

ps = Tweet.find_all("p", {"class": "content"})

counter = 0

for p in ps:
    counter += 1
    print("Tweet No. ", counter, ": ", p.text.strip(), sep="")
    print()

