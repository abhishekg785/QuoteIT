# main.py

from quoteScrapper import Scrapper

def main():
	url = "https://www.brainyquote.com/top_100_quotes"
	quotes = Scrapper(url)
	quotes.scrape_quotes()


if __name__ == '__main__':
	main()