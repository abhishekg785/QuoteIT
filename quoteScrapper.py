"""quoteScrapper.py
simply scrapes the quotes from the website => https://www.brainyquote.com 
"""

import requests		# to get the html page using GET request
from bs4 import BeautifulSoup	# to use html5 parser to create a html parsed tree


class Scrapper(object):

	def __init__(self, url):
		self.url = url
		self.html_text = requests.get(self.url)
		self.html_tree = BeautifulSoup(self.html_text.content, 'html5lib')	# html5lib is the html parser we want to use

	def scrape_quotes(self):
		print self.html_tree




