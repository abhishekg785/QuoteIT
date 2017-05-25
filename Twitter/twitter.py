"""
	author : abhishek goswami
	abhishekg785@gmail.com

	twitter.py 
	for tweeting image to the twitter 
"""

import config

from tweepy import OAuthHandler
from tweepy import API

class Twitter(object):

	def __init__(self):
		try:
			consumer_key = config.CONSUMER_KEY
			consumer_secret = config.CONSUMER_SECRET
			access_token_key = config.ACCESS_TOKEN_KEY
			access_token_secret = config.ACCESS_TOKEN_SECRET
			self.auth = OAuthHandler(consumer_key, consumer_secret)
			self.auth.set_access_token(access_token_key, access_token_secret)
			self.api = API(self.auth, wait_on_rate_limit = True)
			print "Authenticated :)"
		except Exception as err:
			print 'Error occurred!'
			print err


	def post_image(self):
		pass


if __name__ == '__main__':
	obj = Twitter()
	obj.post_image()