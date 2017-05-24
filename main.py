# main.py

import csv

from random import randint

from PIL import Image 
from PIL import ImageDraw
import cStringIO


class QuoteIT(object):

	def __init__(self):
		pass

	def get_random_quote_from_csv(self):
		quotes = []
		rownum = 0;
		file_name = "top_100_quotes.csv"
		with open(file_name, 'rb') as f:
			reader = csv.reader(f)
			for row in reader:
				if rownum == 0:
					header = row
				else:
					text = row[0]
					author = row[1]
					quote = { 'text' : text, 'author' : author }
					quotes.append(quote)
				rownum += 1
			quotes_count = len(quotes)
			random_count = randint(0, quotes_count)
			random_quote = quotes[random_count]
			return random_quote


	def convert_quote_to_image(self):
		pass


if __name__ == '__main__':
	obj = QuoteIT()
	obj.convert_quote_to_image()
	#random_quote = 	obj.get_random_quote_from_csv()