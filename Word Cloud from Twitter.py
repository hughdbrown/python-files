#http://www.techtrek.io/generating-word-cloud-from-twitter-feed-with-python/
#http://sebastianraschka.com/Articles/2014_twitter_wordcloud.html

import tweepy, json, random
from tweepy import OAuthHandler
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from scipy.misc import imread

def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

consumer_key = consumer_key
consumer_secret = consumer_secret
access_token = access_token
access_secret = access_secret
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
  
api = tweepy.API(auth)

f = open('tweets', 'wb')    
 
for status in api.user_timeline():
    f.write(api.get_status(status.id).text.encode("utf-8"))
f.close()

words=' '
count =0
f = open('tweets', 'rb')
for line in f:
    words= words + line.decode("utf-8")
f.close

stopwords = {'https'}

logomask = imread('twitter_mask.png')

wordcloud = WordCloud(
    font_path='/Users/Ryan/Library/Fonts/Inconsolata.otf',
    stopwords=STOPWORDS.union(stopwords),
    #background_color='black',
    background_color='white',
    mask = logomask,
    max_words=500,
    width=1800,
    height=1400
).generate(words)

#plt.imshow(wordcloud.recolor(color_func=grey_color_func, random_state=3))
plt.imshow(wordcloud.recolor(color_func=None, random_state=3))
plt.axis('off')
plt.savefig('./tweetcloud2.png', dpi=300)
plt.show()


