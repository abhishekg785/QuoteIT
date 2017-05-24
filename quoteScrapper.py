"""quoteScrapper.py
simply scrapes the quotes from the website => https://www.brainyquote.com 
"""

import requests		# to get the html page using GET request
from bs4 import BeautifulSoup	# to use html5 parser to create a html parsed tree

import csv	# for creating a csv file of the quotes having quote and the respective author of the quote


class Scrapper(object):

	def __init__(self, url):
		self.url = url
		self.html_text = requests.get(self.url)
		self.html_tree = BeautifulSoup(self.html_text.content, 'html5lib')	# html5lib is the html parser we want to use

	def scrape_quotes(self):
		quotes = []
		quote_section = self.html_tree.find('section', attrs = { 'id' : 'top100' })
		for blackquote in quote_section.findAll('blockquote', attrs = {}):
			quote = {}
			quote_text = blackquote.a.text
			quote_author = blackquote.cite.a.text
			quote['text'] = quote_text
			quote['author'] = quote_author
			quotes.append(quote)
		return quotes

	def generate_quotes_csv(self, quotes, file_name):
		with open(file_name, 'wb') as f:
			w = csv.DictWriter(f, ['text', 'author'])
			w.writeheader()
			for quote in quotes:
				w.writerow(quote)



if __name__ == '__main__':
	url = "https://www.brainyquote.com/top_100_quotes"
	obj = Scrapper(url)
	quotes = obj.scrape_quotes()
	print quotes
	file_name = "top_100_quotes.csv"
	obj.generate_quotes_csv(quotes, file_name)


